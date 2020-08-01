# Working with gradle wrapper

* **To force re-download of dependencies**

  ```gradle
  ./gradlew --refresh-dependencies
  ```

* **To exclude a certain task from being run by gradle**

  Suppose you want to exclude the task `javaDoc` then use `-x` option followed by the task name, i.e `javaDoc` in this case.

  ```gradle
  ./gradlew clean build -x javaDoc
  ```
* **Stop a running gradle build process**

  ```bash
  ./gradlew -stop
  ```

* **Upgrade gradle wrapper to latest release version i.e 6.5**

  Run this inside your project folder via terminal

  ```bash
  ./gradlew wrapper --gradle-version 6.5 --distribution-type all
  ```

* **Make use of Build Cache to speed up your builds.** 

  Set the below property in your global `gradle.properties` file

  ```
  android.enableBuildCache=true
  ```

* **Make your builds faster by building offline** [[Ref Link]](https://medium.com/@cesarmcferreira/mastering-the-terminal-side-of-android-development-e7520466c521#.1cw4bto7f)

  > The `--offline` flag tells gradle to always use dependency modules from the cache, regardless if they are due to be checked again. When running offline, gradle will never attempt to access the network to perform dependency resolution. If required modules are not present in the dependency cache, build execution will fail.

  - Assembling develop debug at full speed:

    ```gradle
    ./gradlew assembleDevelopDebug --offline
    ```

  - Running your unit tests at full speed:

    ```gradle
    ./gradlew test --offline
    ```

* Run a single unit test from the command line using the `--tests` option e.g: `./gradlew testDebugUnitTest --tests "*.MainPresenterTest"` . Use `*` to avoid typing the entire package name. [[Ref Link](https://twitter.com/molsjeroen/status/976469806068256769)]

