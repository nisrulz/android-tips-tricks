# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx[http2]>=0.27",
#     "rich>=13",
# ]
# ///
"""
check_links.py — Link checker for markdown sources (books, docs, READMEs).

Validates every outbound link (http/https) found in the given markdown files
or directories, using uv's single-file script mode:

    uv run scripts/check_links.py src Readme.md
    uv run scripts/check_links.py src -o link-report.md
    uv run scripts/check_links.py src --skip-domain myendpoint.com --skip-domain example.org

What it checks:
  - [text](url) inline markdown links
  - <https://...> angle autolinks
  - bare URLs outside of fenced code blocks and inline code spans

What it reports:
  - DEAD       : 4xx/5xx, DNS failure, timeout, TLS error (after 1 retry)
  - REDIRECT   : link resolves via redirects to a different final URL (200 OK)
  - OK         : 200 OK, no redirect (or same-URL redirect)
  - Special: login-walled pages (e.g. twitter.com/X links return 200 but are
    not publicly viewable) are flagged in --login-gated-domains.

Exits 1 if any DEAD links are found (CI-friendly).
"""

from __future__ import annotations

import argparse
import asyncio
import fnmatch
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import httpx
from rich.console import Console
from rich.table import Table

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

# URLs that are placeholders/examples, not real targets — always skipped.
BUILTIN_SKIP_PATTERNS = [
    "*myendpoint.com*",
    "*example.com*",
    "*example.org*",
    "http://`*",
]

MD_LINK = re.compile(r"\[[^\]]*\]\(\s*<?(https?://[^)\s>]+?)>?\s*\)")
ANGLE_AUTOLINK = re.compile(r"<(https?://[^\s>]+)>")
BARE_URL = re.compile(r"(?<![(<\[])https?://[^\s)\]>,;\"'`]+")
TRAILING_PUNCT = ".,;:)?"

FENCE_RE = re.compile(r"^\s*(```|~~~)")


@dataclass
class Hit:
    url: str
    file: str
    line: int
    status: int = 0  # 0 = network/error
    final_url: str = ""  # set when redirected
    error: str = ""
    outcome: str = "PENDING"  # OK / REDIRECT / DEAD / LOGIN-GATED
    note: str = ""


@dataclass
class Result:
    url: str
    status: int = 0
    final_url: str = ""
    error: str = ""
    hits: list[Hit] = field(default_factory=list)

    @property
    def outcome(self) -> str:
        if self.status in (401, 403):
            return "LOGIN-GATED"
        if self.status in (404, 405, 408, 410, 429, 500, 502, 503, 504):
            return "DEAD"
        if self.status == 0:
            return "DEAD"
        if self.final_url and _normalize(self.final_url) != _normalize(self.url):
            return "REDIRECT"
        if 200 <= self.status < 400:
            return "OK"
        return "DEAD"


def _normalize(u: str) -> str:
    u = u.rstrip("/")
    return u


def is_skipped(url: str, extra_skips: list[str]) -> bool:
    for pat in BUILTIN_SKIP_PATTERNS + extra_skips:
        if fnmatch.fnmatch(url.lower(), pat.lower()):
            return True
    return False


def strip_code(text_lines: list[str]) -> list[str]:
    """Remove fenced code blocks and inline code spans so placeholder URLs
    inside snippets (e.g. http://www.myendpoint.com) are not checked."""
    out, in_fence = [], False
    for line in text_lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            # remove inline code spans
            line = re.sub(r"`[^`]*`", " ", line)
            out.append(line)
    return out


def extract_links(path: Path, extra_skips: list[str]) -> list[Hit]:
    hits: list[Hit] = []
    lines = strip_code(path.read_text(encoding="utf-8", errors="replace").splitlines())
    for i, line in enumerate(lines, start=1):
        candidates: list[str] = []
        for rx, grp in ((MD_LINK, 1), (ANGLE_AUTOLINK, 1), (BARE_URL, 0)):
            for m in rx.finditer(line):
                candidates.append(m.group(grp))
        for url in candidates:
            url = url.rstrip(TRAILING_PUNCT)
            if url.startswith("http") and not is_skipped(url, extra_skips):
                hits.append(Hit(url=url, file=str(path), line=i))
    return hits


async def check(
    client: httpx.AsyncClient, result: Result, sem: asyncio.Semaphore
) -> None:
    url = result.url
    async with sem:
        for attempt in (1, 2):
            try:
                try:
                    r = await client.head(url)
                    if (
                        r.status_code in (404, 405, 403, 408, 501)
                        or r.status_code >= 500
                    ):
                        raise httpx.HTTPError("HEAD rejected")
                except httpx.HTTPError:
                    r = await client.get(url)
                result.status = r.status_code
                result.final_url = (
                    str(r.url)
                    if r.has_redirect_location or r.url != httpx.URL(url)
                    else ""
                )
                if r.status_code in (401, 403):
                    # confirm with GET in case HEAD is walled but page is open
                    try:
                        g = await client.get(url)
                        result.status = g.status_code
                        result.final_url = str(g.url)
                    except httpx.HTTPError:
                        pass
                return
            except Exception as e:  # noqa: BLE001
                result.error = f"{type(e).__name__}: {e}"[:120]
                if attempt == 2:
                    result.status = 0
                await asyncio.sleep(0.8)


async def run(
    paths: list[Path],
    out: Path | None,
    timeout: float,
    concurrency: int,
    skips: list[str],
    login_gated: list[str],
) -> int:
    md_files: list[Path] = []
    for p in paths:
        if p.is_dir():
            md_files.extend(sorted(p.rglob("*.md")))
        elif p.suffix == ".md":
            md_files.append(p)

    hits: list[Hit] = []
    seen: set[str] = set()
    for f in md_files:
        for h in extract_links(f, skips):
            if h.url not in seen:
                seen.add(h.url)
                hits.append(h)

    if not hits:
        print("No links found.")
        return 0

    by_url: dict[str, Result] = {h.url: Result(url=h.url) for h in hits}
    for h in hits:
        by_url[h.url].hits.append(h)

    headers = {"User-Agent": UA, "Accept": "text/html,*/*"}
    sem = asyncio.Semaphore(concurrency)
    async with httpx.AsyncClient(
        http2=True,
        timeout=timeout,
        headers=headers,
        follow_redirects=True,
        verify=True,
    ) as client:
        tasks = [check(client, r, sem) for r in by_url.values()]
        done = 0
        for fut in asyncio.as_completed(tasks):
            await fut
            done += 1
            if done % 25 == 0 or done == len(tasks):
                print(f"  …{done}/{len(tasks)} checked")

    console = Console()
    counts = {"OK": [], "REDIRECT": [], "LOGIN-GATED": [], "DEAD": []}
    for r in by_url.values():
        counts[r.outcome].append(r)

    table = Table(
        title=f"Link check — {len(by_url)} unique links, {len(md_files)} files"
    )
    table.add_column("Outcome", style="bold")
    table.add_column("Count", justify="right")
    table.add_column("")
    colors = {
        "OK": "green",
        "REDIRECT": "yellow",
        "LOGIN-GATED": "magenta",
        "DEAD": "red",
    }
    for name in ("OK", "REDIRECT", "LOGIN-GATED", "DEAD"):
        table.add_row(name, str(len(counts[name])), "", style=colors[name])
    console.print(table)

    def section(title: str, results: list[Result]) -> None:
        if not results:
            return
        console.print(f"\n[bold {colors[title]}]{title} ({len(results)})[/]")
        for r in sorted(results, key=lambda x: x.url):
            loc = ", ".join(f"{h.file}:{h.line}" for h in r.hits[:3])
            extra = ""
            if r.outcome == "REDIRECT":
                extra = f" → {r.final_url}"
            elif r.status == 0:
                extra = f" ({r.error})"
            elif r.status:
                extra = f" (HTTP {r.status})"
            console.print(f"  {r.url}[dim]{extra}[/dim]")
            console.print(f"    [dim]↳ {loc}[/dim]")

    section("DEAD", counts["DEAD"])
    section("LOGIN-GATED", counts["LOGIN-GATED"])
    section("REDIRECT", counts["REDIRECT"])

    # Note login-gated-looking domains explicitly
    flagged = [
        r
        for r in by_url.values()
        if any(fnmatch.fnmatch(r.url, pat) for pat in login_gated)
        and r.outcome not in ("DEAD",)
    ]
    if flagged:
        console.print(
            "\n[bold magenta]Note:[/bold magenta] links in login-gated domains return HTTP 200 "
            "but require an account to view publicly:"
        )
        for r in flagged:
            console.print(f"  {r.url}")

    if out:
        with out.open("w", encoding="utf-8") as fh:
            fh.write("# Link check report\n\n")
            fh.write(f"Files: {', '.join(str(p) for p in md_files)}\n\n")
            for name in ("DEAD", "LOGIN-GATED", "REDIRECT", "OK"):
                fh.write(f"## {name} ({len(counts[name])})\n\n")
                for r in sorted(counts[name], key=lambda x: x.url):
                    for h in r.hits:
                        suffix = ""
                        if r.outcome == "REDIRECT":
                            suffix = f" → {r.final_url}"
                        elif r.status == 0:
                            suffix = f" ({r.error})"
                        elif r.status:
                            suffix = f" (HTTP {r.status})"
                        fh.write(f"- `{h.file}:{h.line}` [{h.url}]({h.url}){suffix}\n")
                fh.write("\n")
        print(f"\nMarkdown report written to {out}")

    dead = len(counts["DEAD"])
    print(
        f"\nSummary: {len(counts['OK'])} OK · {len(counts['REDIRECT'])} redirected · "
        f"{len(counts['LOGIN-GATED'])} gated · {dead} dead"
    )
    return 1 if dead else 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Validate outbound links in markdown files."
    )
    ap.add_argument(
        "paths", nargs="+", type=Path, help="markdown files or directories to scan"
    )
    ap.add_argument(
        "-o", "--output", type=Path, default=None, help="write markdown report here"
    )
    ap.add_argument("--timeout", type=float, default=10.0)
    ap.add_argument("--concurrency", type=int, default=10)
    ap.add_argument(
        "--skip",
        action="append",
        default=[],
        metavar="PATTERN",
        help="glob pattern of URLs to skip (repeatable), e.g. --skip '*appspot.com*'",
    )
    ap.add_argument(
        "--login-gated",
        action="append",
        default=["*twitter.com/*", "*x.com/*"],
        metavar="PATTERN",
        help="glob pattern of login-walled domains (repeatable)",
    )
    args = ap.parse_args()

    missing = [p for p in args.paths if not p.exists()]
    if missing:
        print(f"paths not found: {missing}", file=sys.stderr)
        return 2

    return asyncio.run(
        run(
            paths=args.paths,
            out=args.output,
            timeout=args.timeout,
            concurrency=args.concurrency,
            skips=args.skip,
            login_gated=args.login_gated,
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
