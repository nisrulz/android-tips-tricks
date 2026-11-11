# Modern Android Tips

## Secrets and security

* **Assume the APK is fully compromised**

  Anyone with the APK has full read access ([`jadx`](https://github.com/skylot/jadx)/[`apktool`](https://apktool.org)) and full runtime control ([Frida](https://frida.re) on a rooted device), with unlimited time. If the app can compute a secret, an attacker can make it compute it and read it from memory. Keep as few secrets on the device as you can get away with, and verify clients on your server instead.

* **Never ship API keys via hardcoded constants or `buildConfigField`**

  Both bake the value as a plaintext string constant into the DEX string pool; [R8](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) obfuscation does not touch string contents. Unzip the APK, open `classes.dex` in `jadx-gui`, search. Extracting it takes five minutes.

  ```groovy
  buildTypes {
    release {
      buildConfigField "String", "API_KEY", "\"sk_live_...\""  // still plaintext in DEX
    }
  }
  ```

* **Don't rely on native code (NDK) to hide secrets**

  `strings libnative-lib.so` finds plaintext; obfuscation logic is traceable in [Ghidra](https://github.com/NationalSecurityAgency/ghidra)/[IDA](https://hex-rays.com/ida-pro/). Dynamic extraction is even easier: hook the JNI export with Frida and print the return value as the app hands it back to Java.

* **Split-key tricks only move the weak point**

  Combining halves in native code still produces the full plaintext in process memory before the request is signed. Attackers hook the combine function, intercept the runtime-half fetch, or dump memory at the network call.

* **Keep secrets off the device with a backend-for-frontend (BFF)**

  The app authenticates to *your* backend (session token, JWT, mTLS); your backend holds the third-party secret and forwards the call. Bonus: rate limiting, secret rotation without an app update, and revocable client credentials.

* **Protect sensitive endpoints with nonce + [Play Integrity](https://developer.android.com/google/play/integrity) attestation**

  Client fetches a one-time nonce, attaches a Play Integrity token (genuine binary, legit install, untampered device), and the backend verifies both with hard rejection. Note: Play Integrity is probabilistic trust, not a cryptographic guarantee.

* **Audit your own release builds**

  Decompile your own APK and grep for keys before someone else does. If a device secret is unavoidable, RASP and build-time string encryption raise cost but never make extraction impossible.

* **Pin the server certificate or public key with [OkHttp](https://lysine.dev/okhttp/)'s `CertificatePinner`**

  Pinning blocks MITM attacks and protects you even if a CA is compromised, since the app trusts only the pinned cert/key during the TLS handshake. Prefer public-key pins and include a backup key to ease rotation.

  ```kotlin
  val certificatePinner = CertificatePinner.Builder()
      .add("your-server.com", "sha256/your_certificate_hash")
      .build()
  val okHttpClient = OkHttpClient.Builder()
      .certificatePinner(certificatePinner)
      .build()
  ```

* **Plan for pin expiry before you pin**

  Pins must be updated and the app re-shipped when certs rotate; add fallback mechanisms and only pin sensitive data flows, since overuse creates maintenance burden.

## Kotlin flows: StateFlow and SharedFlow

* **Pick the flow type by job: `Flow` for one-shot cold streams, `StateFlow` for state, `SharedFlow` for one-off events**

  [StateFlow](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow) always holds the last value (`replay = 1`, needs an initial value); SharedFlow's default `replay = 0` means emissions before a subscriber are lost, which is exactly what you want for snackbars and navigation, so stale events don't re-appear after rotation.

* **Convert cold repository flows to hot before exposing them**

  Every new subscriber to a cold flow restarts the upstream work. Use `stateIn`/`shareIn` in the ViewModel:

  ```kotlin
  repo.getUsers().stateIn(
      scope = viewModelScope,
      initialValue = UiState.Loading,
      started = SharingStarted.WhileSubscribed(5000L)
  )
  ```

* **Use `SharingStarted.WhileSubscribed(5000L)` for ViewModel state**

  Upstream starts with the first subscriber and stops 5s after the last leaves, surviving config changes without wasting resources. `Eagerly`/`Lazily` never stop upstream.

* **Update `MutableStateFlow` atomically with `.update { }`**

  Prefer `_userFlow.update { ... }` over `_userFlow.value =` (also `getAndUpdate`, `updateAndGet`; `tryEmit(value): Boolean` for SharedFlow).

* **Collect flows lifecycle-aware, not in `launch` alone**

  [Collect](https://developer.android.com/topic/libraries/architecture/lifecycle) only between STARTED and STOPPED to save resources:

  ```kotlin
  lifecycleScope.launch {
      lifecycle.repeatOnLifecycle(Lifecycle.State.STARTED) {
          viewModel.userFlow.collect { render(it) }
      }
  }
  ```

  In Compose: `collectAsStateWithLifecycle()`.

* **Back UI state with `SavedStateHandle.getStateFlow()`**

  It replaces the backing [`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle) and survives process death. Keep payloads `@Parcelize` and small (avoid `TransactionTooLargeException`); call refresh logic only when `savedInstanceState == null`.

* **Know StateFlow's conflation when testing**

  `emit(Error)` before a subscriber collects means they only ever see `Error`, never the prior `Success`. Assert StateFlow via `.value` (non-suspending); test SharedFlow with [Turbine](https://github.com/cashapp/turbine) (`test { awaitItem() }`), and manually collect `stateIn` flows in tests with `UnconfinedTestDispatcher` then cancel.

## Compose and sensors

* **Trace recomposition causes with [ComposeInvestigator](https://jisungbin.github.io/ComposeInvestigator/)**

  A Compose compiler plugin (no boilerplate, no API calls) that reports whether a composable was skipped, which arguments changed, which internal state changed, and the call stack leading to invocation, which helps when the same composable is reused in several places.

  ```kotlin
  plugins { id("in.sungb.composeinvestigator") version "<version>" }
  ```

* **Get device orientation with the Fused Orientation API instead of raw sensor math**

  `play-services-location` 21.2.0+ fuses accelerometer, gyroscope, and magnetometer into one provider (no Google Services registration, no permission up to 200Hz on Android S+):

  ```kotlin
  val client = LocationServices.getFusedOrientationProviderClient(context)
  val request = DeviceOrientationRequest.Builder(
      DeviceOrientationRequest.OUTPUT_PERIOD_DEFAULT).build()  // 50Hz compass; MEDIUM=100Hz gestures, FAST=200Hz AR
  client.requestOrientationUpdates(request, executor, listener)
  ```

* **Derive the rotation matrix directly from `DeviceOrientation.getAttitude()`**

  No more manual accelerometer+magnetometer `SensorManager.getRotationMatrix` calls:

  ```kotlin
  SensorManager.getRotationMatrixFromVector(rotationMatrix, deviceOrientation.getAttitude())
  ```

* **Switch to the main dispatcher before touching UI state from orientation callbacks**

  Samples arrive on a background thread and only while the app is foregrounded; wire start/stop to lifecycle (`LifecycleEventObserver` on ON_START/ON_STOP) and share one executor across jobs.

## Testing with the Robot pattern

* **Wrap each screen in a Robot instead of raw `ComposeTestRule` calls**

  Direct node queries get repetitive and unreadable fast; a robot per screen/flow makes tests read like user behavior and keeps each screen's actions in one place.

  ```kotlin
  with(FirstScreenRobot(composeTestRule)) {
      assertMainContent()
      clickNext()
  }
  with(SecondScreenRobot(composeTestRule)) { assertSecondScreen() }
  ```

* **Put shared actions in an abstract base Robot; keep screen-specific methods in screen robots**

  The base class holds only calls you do all the time (`clickTextButton`, `clickIconButton`, `assertText`, `goBack`, `waitFor`); the template shouldn't absorb screen logic.

* **Chain multiple robots to test multi-screen navigation**

  One test can walk the whole app by mixing robots (`MainRobot` → `NavigationRobot.openSettingsScreenViaDrawer()` → `MainSettingsRobot...`), keeping each screen's assertions where they belong.

* **Assert Compose UI state via semantics like `stateDescription`**

  E.g. distinguish animation on/off by matching `hasStateDescription("Turned on")` rather than waiting on visuals.

## Gradle convention plugins

* **Stop configuring submodules top-down from the root build file**

  `subprojects {}` blocks with `if` guards hide where configuration comes from, tightly couple modules to the root, and bloat with if-else as module types diverge. Convention plugins apply build logic only to modules that need it.

* **Start with [`buildSrc`](https://docs.gradle.org/current/userguide/sharing_build_logic_between_subprojects.html) and precompiled script plugins**

  Drop a `.gradle.kts` file in `buildSrc/src/main/kotlin` named after the plugin; apply by id. Kotlin DSL only (not Groovy):

  ```kotlin
  // buildSrc/src/main/kotlin/test-configuration.gradle.kts
  tasks.withType<Test> {
      useJUnitPlatform()
      testLogging { events(TestLogEvent.FAILED); exceptionFormat = TestExceptionFormat.FULL }
  }
  ```

  ```kotlin
  plugins { id("test-configuration") }
  ```

* **Chain convention plugins to compose module archetypes**

  A `ktor-configuration` plugin can apply the Ktor plugin *and* an `owasp-configuration` plugin, so modules end up with one-line build files. Note: inside a precompiled script you must reference other plugins by `id(...)`, because version catalogs are not available in the plugins block.

* **Add plugins your script needs as `compileOnly` dependencies in buildSrc**

  A precompiled script that configures `Test` tasks needs the Kotlin JVM plugin to compile:

  ```toml
  kotlinJvmLib = { module = "org.jetbrains.kotlin.jvm:org.jetbrains.kotlin.jvm.gradle.plugin", version.ref = "kotlinVersion" }
  ```

  ```kotlin
  // buildSrc/build.gradle.kts
  dependencies { compileOnly(libs.kotlinJvmLib) }
  ```

* **Move to a `build-logic` [composite build](https://docs.gradle.org/current/userguide/composite_builds.html) when buildSrc slows incremental builds**

  Any change to buildSrc makes the whole project out-of-date. Register it via `pluginManagement { includeBuild("build-logic") }` with a `:convention` module using `kotlin-dsl` for faster incremental builds.

* **Register convention plugins with a `gradlePlugin { plugins { register(...) } }` block, then apply via version catalog**

  Add them to [`libs.versions.toml`](https://docs.gradle.org/current/userguide/version_catalogs.html) with `version = "unspecified"` so modules use type-safe aliases:

  ```toml
  [plugins]
  newslayer-android-application = { id = "newslayer.android.application", version = "unspecified" }
  ```

  ```kotlin
  plugins { alias(libs.plugins.newslayer.android.application) }
  ```

* **Keep plugin implementations small with shared helper functions**

  E.g. `fun Project.configureKotlinAndroid(commonExtension: CommonExtension<*,*,*,*,*>)` sets compileSdk/minSdk/compileOptions once; a `libs` accessor (`extensions.getByType<VersionCatalogsExtension>().named("libs")`) brings the catalog into plugin code for dependencies.

* **Declare build tools as `compileOnly` in the convention module and validate strictly**

  `compileOnly(libs.android.gradlePlugin, libs.kotlin.gradlePlugin, ...)`; enable `validatePlugins { enableStricterValidation = true; failOnWarning = true }`, plus `org.gradle.caching=true` and the [configuration cache](https://docs.gradle.org/current/userguide/configuration_cache.html) (`org.gradle.configuration-cache=true`).

## Shipping and rollout

* **Never release to 100%, use a staged rollout**

  You can't recall a mobile release; users keep running a broken build until they update (80% update in ~5 days, 2-5% never). A common 7-day ramp: 1% → 2% → 5% → 10% → 20% → 50% → 100%. Halting stops new users from getting the update but doesn't roll back those who already have it.

* **Release in the morning and monitor during working hours**

  Never ship late in the day or on a Friday. Watch [Crashlytics](https://firebase.google.com/docs/crashlytics) at 1% for fresh and regressed issues; enable velocity alerts (fire within an hour when crash-free sessions drop past your threshold, ≥250 sessions).

* **Provision remote feature flags so you can kill a faulty feature without an app update**

  [Firebase Remote Config](https://firebase.google.com/docs/remote-config) or your own remote config lets you toggle off crashing behavior in real time while you fix and ship:

  ```kotlin
  if (RemoteConfigRepository.isFeatureColorNameEnabled()) { /* new path */ }
  else { /* old/safe path */ }
  ```

* **Define feature flags as enums implementing a common `Feature` interface**

  Enums force exhaustive `when` handling and let you auto-generate a debug toggle UI over `FeatureFlag.values()`. Gate providers by `hasFeature()` so unfinished features are never accidentally shipped via tool defaults (e.g. Firebase returning `false` when no value exists).

* **Resolve flags through a prioritized provider chain**

  Providers by priority: test overrides > Firebase (gradual rollout) > debug SharedPreferences overrides > store baseline for release. Give each provider an explicit value per feature so nothing ships half-done; remove the flag and dead code once rollout completes.

* **Gate flags at compile time with LINE's [`feature-flag-android`](https://github.com/line/feature-flag-android) Gradle plugin**

  Flags come from a property file and compile to booleans, enabled by variant, version (`FLAG_2 = 1.2.0~`), user, another flag, or combinations, plus `PRIVATE`, `OVERRIDABLE`, and `LITERALIZE` modifiers.

  ```kotlin
  plugins { id("com.linecorp.android.feature-flag") version "<version>" }
  featureFlag {
      sourceFiles.setFrom(file("FEATURE_FLAG"))
      packageName = "com.example.featureflag"
  }
  ```

* **Keep the debug flag-toggle UI out of release builds**

  Put it in a separate module included only for debug: `debugImplementation(project(":features:test-settings"))`, with business logic in a `feature-flags` library module.

* **Replacing Firebase Remote Config is a systems-design problem as much as a dependency swap**

  The SDK silently guaranteed cold-start behavior, crash-safe cache writes, cross-process reads, and thread safety. Rebuild: three-layer fallback (server → last good disk value → baked-in defaults), atomic temp-file-then-swap writes, one writer process with many readers, bounded startup waits, and conditional refresh via ETag.

* **Route all config reads through a single object ("one door") before migrating call sites**

  Build the single object owning the fallback chain first, then move the call sites behind it; otherwise you'll find leftover SDK references only by searching the whole codebase, not reviewing diffs. Document load-bearing rules ("only one process writes", "can block up to 3s") where the next person sees them.

## Verifying AI-generated code

* **A green test suite does not mean it works on a phone**

  AI agents work on the repository; Android correctness depends on the device. Process death, OEM battery managers, R8, unexpected recomposition, and main-thread work on low-memory devices rarely show in a diff or on a flagship emulator. An agent working toward green sometimes takes the shortest path: through the test file.

* **Prefer `SavedStateHandle` over plain `mutableStateOf` for restorable state**

  Both compile and pass simple unit tests, but only one survives Android killing the app in the background:

  ```kotlin
  class ComposeViewModel(private val state: SavedStateHandle) : ViewModel() {
      val draft = state.getStateFlow("draft", "")
      fun onDraftChange(text: String) { state["draft"] = text }
  }
  ```

* **Make checking cheaper than generating**

  Background the app and run `adb shell am kill <package>` to test process death; smoke-test the critical flow on the minified release build (catches R8 removals); add one [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) for startup/scroll; keep agent diffs small and read any edited tests first; read [Perfetto](https://perfetto.dev/) traces and heap dumps yourself.

* **Treat `AppFunctions` KDoc as a contract and validate every argument**

  On Android 16+, exposed functions are called by agents that read the KDoc as their description; every argument is LLM-generated input and must be validated like any untrusted input.

## Kotlin and Java utilities

* **Measure elapsed time with `System.nanoTime()`, never `currentTimeMillis()`**

  `currentTimeMillis()` self-corrects and can stay static or even go backwards; `nanoTime()` is monotonic and measures intervals only.

  ```java
  long start = System.nanoTime();
  // ... code to measure ...
  long elapsedNanos = System.nanoTime() - start;
  ```

* **Share content to social apps via their intent URL schemes**

  URL-encode text (`%0A` = newline):

  - Threads: `https://www.threads.net/intent/post?text=<text>`
  - X: `https://twitter.com/share?text=<text>&url=<url>&via=<handle>`
  - WhatsApp: `https://api.whatsapp.com/send?text=<text>`
  - Telegram: `https://t.me/share/url?url=<url>&text=<text>`
  - LinkedIn: `https://www.linkedin.com/shareArticle?url=<url>&source=<source>`
