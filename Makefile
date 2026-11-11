.PHONY: help build serve clean deploy check-links

# Default target
help: ## List available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

build: ## Build the book (outputs to book/)
	mdbook build

serve: ## Build and serve locally with live reload, opens the browser
	mdbook serve --open

clean: ## Remove build artifacts (book/)
	mdbook clean

deploy: ## Build and publish to GitHub Pages (gh-pages branch)
	./deploy-to-github-pages.sh

check-links: ## Validate all outbound links in the book sources
	uv run scripts/check_links.py src Readme.md -o $(REPORT)

REPORT ?= link-report.md
