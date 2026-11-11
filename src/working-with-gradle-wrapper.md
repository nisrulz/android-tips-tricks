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

* **Upgrade gradle wrapper to latest release version (check [gradle.org/releases](https://gradle.org/releases/) for the current one, i.e 9.8.2)**

  Run this inside your project folder via terminal

  ```bash
  ./gradlew wrapper --gradle-version 9.8.2 --distribution-type all
  ```

* **Make your builds faster by building offline**

  > The `--offline` flag tells gradle to always use dependency modules from the cache, regardless if they are due to be checked again. When running offline, gradle will never attempt to access the network to perform dependency resolution. If required modules are not present in the dependency cache, build execution will fail.

  - Assembling develop debug at full speed:

    ```gradle
    ./gradlew assembleDevelopDebug --offline
    ```

  - Running your unit tests at full speed:

    ```gradle
    ./gradlew test --offline
    ```

* Run a single unit test from the command line using the `--tests` option e.g: `./gradlew testDebugUnitTest --tests "*.MainPresenterTest"` . Use `*` to avoid typing the entire package name.

