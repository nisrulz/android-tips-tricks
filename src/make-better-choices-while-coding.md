# Make better choices while coding

- **Use OkHttp over HttpUrlConnect**

  HttpUrlConnect suffers from [quite some bugs](https://android-developers.googleblog.com/2011/09/androids-http-clients.html). [Okhttp](https://lysine.dev/okhttp/) solves them in a more elegant manner. [[Reference Link]](https://corner.squareup.com/2013/05/announcing-okhttp.html)

* **Use [Pidcat](https://github.com/JakeWharton/pidcat) for a better log reading experience**

* **Use some Version Control System(VCS) like [Git](https://git-scm.com/)**

* **Use [ClassyShark](https://github.com/google/android-classyshark)**

  It is a standalone tool for Android Devs used to browse any Android executable and show important info such as class interfaces and members, dex counts and dependencies

* **Use [Stetho](https://github.com/meta/stetho)**

  Debug your android apps using Chrome Dev Tools. Includes tools like Network Monitor, Shared Preference explorer etc.

* **Use [Battery Historian](https://github.com/google/battery-historian)**

  A tool to analyze battery consumers using Android "bugreport" files.

* **Always use a constant version value like "1.2.0"**

  Avoid using `+` when specifying the version of dependencies.

  - Keeps one secured from unexpected API changes in the dependency.
  - Avoids doing an extra network call for the checking latest version of each dependency on every build.

* **[Do not use your own personal email for Google Play Developer Account](https://www.reddit.com/r/Android/comments/2hywu9/google_play_only_one_strike_is_needed_to_ruin_you/)**
* **Use Vectors instead of PNG**

  If you do **have** to use png, compress them. Take a look at [TinyPNG](https://tinypng.com).

* **Learn about some architecture such as MVP or Clean**

* **Try to understand and follow TDD (Test Driven Development)**

* **Follow the DRY principle**
  DRY = Do not Repeat Yourself

* **Package by Feature, not layers**

* **[Learn about Dependency Resolution](https://crushingcode.nisrulz.com/blog/the-curious-case-of-dependency-conflicts/)**

  With the speed android dependencies update, sooner or later you are going to encounter some sort of dependency conflict. The solution is making use of Dependency Resolution. [Official Reference](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.ResolutionStrategy.html)


* **If you’re creating a gradient in xml with a part being completely transparent, be really careful when using `@android:color/transparent`**

* **[Follow a standard naming convention for your resources](https://jeroenmols.com/blog/2016/03/07/resourcenaming/)**

* **Use a proper .gitignore in your Android Projects, [Check it here](/android.gitignore)**

* **[Use LeakCanary to detect memory leaks in your app](https://github.com/square/leakcanary)** - Its a memory leak detection library for Android and Java.

* **Enable gradle to automatically download missing platforms in android sdk**

  Set the below property in your global `gradle.properties` file

  ```
  android.builder.sdkDownload=true
  ```

  > This is an experimental option and it only downloads build tools and platforms, but doesn't actually update Google or Support repository [[Bug Ref]](https://code.google.com/p/android/issues/detail?id=212309)


* **Clear your gradle cache if you think that bundled support and google play services lib in android sdk are inconsistent**

  - Goto `~/.gradle/caches/` and delete everything inside the `cache` folder.
  - Open SDK Manager and resync all support libs and google play services
  - Next re-sync your project
  - Everything should become consistent and functional.

* **Use [`alfi`](https://github.com/cesarferreira/alfi) to find the gradle dependency statement for a library**

  - Run

    ```bash
    alfi name_of_library
    ```

  - Copy the desired library
  - Paste in your build.gradle

* **Use [`dryrun`](https://github.com/cesarferreira/dryrun) to test a library directly**

  - Just Run

    ```bash
    dryrun REMOTE_GIT_URL
    ```


* **Use an abtracted [Logger](/Logger.java) class**

* **If you want to automatically initialize your library, use a Content Provider** [[Read how Firebase does it - Ref Link]](https://firebase.googleblog.com/2016/12/how-does-firebase-initialize-on-android.html)

* **Reduce installed app size with `useLegacyPackaging`**

  Set `useLegacyPackaging = false` on your JNI libs packaging options (AGP does this by default for `minSdk` 23+). This prevents the system from creating a second copy of the `.so` files and lets it load native libs straight from the APK, no code changes on your part required. This replaces the older `android:extractNativeLibs="false"` manifest attribute.

* **Selectivily execute a specific method in Android Studio**

  ![Image](img/selectiverun.gif)

* **Did you get one of these Google Play Developer Policy Violation Emails? Worry not, generate a Privacy Policy for your android app**

  - Take a look at [App Privacy Policy Generator](https://app-privacy-policy-generator.firebaseapp.com/), a web app to generate a generic privacy policy for your app.

* **Activity LifeCycle**

  ![diagram](img/activityStateDiagram.jpeg)

* **Tip about `onSaveInstanceState()`**  
  `onSaveInstanceState()` is called **_only when the OS decides to kill the `Activity` instance_**. It will not be called when Activity is explicitly killed i.e User pressed back button or `finish()` is called from code.

* **[Read about whats in an APK here](https://crushingcode.nisrulz.com/blog/whats-in-the-apk/)**

* **[Input some text in an editfield in a running emulator from your keyboard ](https://fragmentedpodcast.com/episodes/77/)**

  ```gradle
  adb shell input text "keyboard text"
  ```

* **Use [`areNotificationsEnabled()`](<https://developer.android.com/reference/androidx/core/app/NotificationManagerCompat.html#areNotificationsEnabled()>) from [`NotificationManagerCompat`](https://developer.android.com/reference/androidx/core/app/NotificationManagerCompat.html) to detect whether your users blocked your Notifications**

* **Don't hard-code encryption keys, a simple grep for `"Ljavax/crypto"` reveals them in bytecode**

* **Intents have a limited payload size (1Mb), don't serialize and attach entire file to it**

* **Always copy a file before sending it as intent URI. Receiving app could edit it & send a canceled result**

* **Use `https://` as scheme for app deeplinks, Android App Links verification requires it and when app not installed it drives users to a domain you own**

* **Use below to display your app launch time**

  ```bash
  adb shell am start -W <packagename>/. <activityname>
  ```

* **Use activity-alias or your launcher icons will disappear when renaming/moving your MainActivity**

* To testout doze mode, trigger it using `adb` [[Ref Link](https://developer.android.com/training/monitoring-device-state/doze-standby#testing_doze)

  ```bash
  adb shell dumpsys deviceidle force-idle
  ```

* Thumb rule regarding setting `compileSdkVersion`, `minSdkVersion` and `targetSdkVersion`

  > `minSdkVersion` (lowest possible) <= `targetSdkVersion` == `compileSdkVersion` (latest SDK)

- Google released an option to include OSS license activity in your app, use that to attribute credits to the OSS libs in your app [[Ref Link](https://developers.google.com/android/guides/opensource)]

  > [Checkout a working example here](https://github.com/nisrulz/android-examples/tree/master/OSSLicenseActivity)

- Make Android Studio render `<merge>` layouts correctly by specifying the layout type with the tools:parentTag attribute

  ![diagram](img/mergetaginlayout.jpg)

- Checkout the Background Execution Limits introduced in Android Oreo and update your app to work with the restrictions

- To take good screenshots with clean status bar use the [**Demo Mode**](https://android.googlesource.com/platform/frameworks/base/+/master/packages/SystemUI/docs/demo_mode.md) in Android

  - Steps

    1.  Enable Demo Mode

        ```bash
        adb shell settings put global sysui_demo_allowed 1
        ```

    1.  Enable/disable icons by running the right command

        ```bash
        // display time 12:00
        adb shell am broadcast -a com.android.systemui.demo -e command clock -e hhmm 1200

        // Display full mobile data without type
        adb shell am broadcast -a com.android.systemui.demo -e command network -e mobile show -e level 4 -e datatype false

        // Hide notifications
        adb shell am broadcast -a com.android.systemui.demo -e command notifications -e visible false

        // Show full battery but not in charging state
        adb shell am broadcast -a com.android.systemui.demo -e command battery -e plugged false -e level 100
        ```

    1.  Run app and take screenshots

    1.  Exit demo mode once you are done

        ```bash
        adb shell am broadcast -a com.android.systemui.demo -e command exit
        ```

- To record video of your android device [[Ref Link](https://dev.to/aneesahammed/best-way-to-record-your-screen-on-android)]

  ```bash
  adb shell && screenrecord /sdcard/download/fileName.mp4
  ```

  > Hit `Ctrl+C` to exit/stop recording
  >
  > Recorded video file is saved at the location mentioned in the command on the device itself.

- Use Dao inheritance to reduce the amount of boilerplate code [[Ref Link](https://gist.github.com/florina-muntenescu/1c78858f286d196d545c038a71a3e864)]

- Instead of using `getActivity()` in fragment, keep a habit of getting context from `onAttach()`.

- Avoid setting a background in every view/fragment as it likely causes overdraw.

- `View.getWidth() = 0?` That's because your view hasn't been layout yet, use globallayoutListener to know layout done.

- Android never kills activities, it only kills processes. When low memory the lowest priority ranked will be killed.

- Use `.([filename].java:[line])` in your log statements to make them clickable in Android Studio and Intellij IDEA.

- Use `-whyareyoukeeping class com.jeroenmols.MyClass` to figure out why certain a class wasn't removed.

- Use certificate pinning to resist impersonation by attackers using mis-issued or otherwise fraudulent certificates, when making requests from your app. [[Ref Link](https://dev.to/mplacona/certificate-pinning-in-android)]

- Do download the latest emulator using CLI

  ```
  cd <android_sdk>/tools/bin
  ./sdkmanager --channel=3 emulator
  ```

  To check the version of emulator, use `./sdkmanager --channel=3 emulator`

- **Checkout some tricks when using Android Strings in XML**

- **Checkout some cool tricks when using `tools:` attribute in your android layouts, such as sample data and recyclerview item layout previews [here](https://blog.stylingandroid.com/tool-time-part-1-2/)**

- Remove all debug log statements from the release build using the below proguard rules. (app's build.gradle should have `minifyEnabled true` set for this to work)

  ```
  # Remove all debug logs
  -assumenosideeffects class android.util.Log {
      public static *** d(...);
  }
  ```

  > The above snippet is usually appended to contents of app/proguard-rules.pro file

* **[Should I use Enums in Android?]**

  **tl;dr**

  - If you need code to be very performant integer constants may be the way to go
    ```java
    public class Operator {
        public static final int ADD = 1;
        public static final int SUBTRACT = 2;
        public static final int MULTIPLY = 3;
        public static final int DIVIDE = 4;
    }
    ```
  - Use Enums because

    - Are type-safe, so you can only use valid enum types
    - Provide better code readability
    - Can implement interfaces
    - Support polymorphic behavior
    - In some really trivial cases, Proguard can optimize Enums into integer constants for you [[Ref Link](https://www.guardsquare.com/manual/configuration/optimizations)]
    - Performance difference rarely makes a difference.

    ```java
    public enum Operators {
        Add, Subtract, Multiply, Divide
    }
    ```

- The string resource `android.R.string.yes` doesnot yield string "Yes" instead it yields "Ok". Similarly the string resource `android.R.string.no` doesnot yield string "No" instead it yields "Cancel"

  ![string resource](img/android_str_mismatch.jpg)

- Don’t want generated files in your AS search results? Go to `Preferences -> File Types -> Ignore files and folders` and add the pattern to ignore - e.g. `*.dex;*.class;`

- If you uncheck “Suspend” and check “Evaluate and Log” in breakpoint menu, the breakpoint will print evaluated statement into the uncluttered “Console” window. No need for recompile due to added Log.d statements anymore

  ![Breakpoint Logs](img/breakpoint_logs.jpg)

- If you're working with Android Things and you don't have an extrenal screen for your device, install [scrcpy](https://github.com/Genymobile/scrcpy) and use it to see what's going on your Android IoT device. It works a charm over wireless adb.

- Android Studio has this weird behaviour that it allows to edit its default code style, which leads to a weird side-effect. If you open your pre-setup project(with set codestyle and copyright configs) in Android Studio it will delete all pre-setup codestyle and copyright profile in this project. This is every much evident if you checked in your configs into git for sharing purpose, which is lost immediately as soon as you open the project

  ```bash
  deleted:    .idea/codeStyles/Project.xml
  deleted:    .idea/codeStyles/codeStyleConfig.xml
  deleted:    .idea/copyright/profiles_settings.xml
  deleted:    .idea/copyright/copyright.xml
  ```

  To fix that please follow along as below: [All thanks to Said Tahsin Dane for the solution]

  - We first need to verify that your `Default` codestyle isn't modified. To check that please open Android Studio with any project except your pre-setup(with set codestyle and copyright configs) project. Then navigate to `Preferences>Edior>Codestyle` and check if your code scheme has `Default` in **BLUE** color (this means it is modified).

    ![modified_default](img/modified_default.png)

  - However if it is not colored **BLUE**, you are good and you can go ahead to open your pre-setup(with set codestyle and copyright configs) project and everything should be pre-setup for you.

  - If it is modified (colored **BLUE**), then click on the cog icon and select `Restore Default`

    ![restore_default](img/restore_default.png)

  - After you hit that option, simply accept the change

    ![accept_change](img/accept_change.png)

  - Once done, you will see your Default is no more colored **BLUE** or modified, which means you are good

    ![unmodified_default](img/unmodified_default.png)

  - Now simply go ahead and open your pre-setup(with set codestyle and copyright configs) project and everything should be pre-setup for you.

- If you add `android:sharedUserId` to an already published app, the app data will be cleared for all users that install your upgrade (because Android changes the process). So if you ever intend to use it, you must add it before publishing your app

- When opening up methods for testing, use otherwise to still hide it from code complete. [VisibleForTesting plugin](https://plugins.jetbrains.com/plugin/9952-visiblefortesting)

  ![making_methods_visible_for_testing](img/making_methods_visible_for_testing.jpg)

- You can group your recent Android Studio projects, and add icons to them

  ![group_recent_projects](img/group_recent_projects.jpg)

- Only build a single configuration to speed up debug builds.

  ![build_single_config](img/build_single_config.jpg)

- Avoid the annoying jump to Design tab while editing XML. Prefer XML editor under Settings

  ![set_xml_as_preferred](img/set_xml_as_preferred.jpg)

- Improve Android Studio code inspections with Thread annotations [[Ref Link](https://developer.android.com/studio/write/annotations#thread-annotations)]

  <img src="img/thread_annotations.jpg" width="600"/>

- Use `adb` to put a phone into doze mode for testing [[Ref Link](https://developer.android.com/training/monitoring-device-state/doze-standby#testing_doze)]

  <img src="img/testing_doze_mode.jpg" width="600"/>

- Use `areNotificationsEnabled()` from `NotificationManagerCompat` to detect whether your users blocked your Notifications [[Ref Link](<https://developer.android.com/reference/androidx/core/app/NotificationManagerCompat.html#areNotificationsEnabled()>)]

  <img src="img/are_notification_enabled.jpg" height="400"/>

- `Activity.runOnUiThread` is just a convenient wrapper of `Handler.post`; don't pass around `Activity` just so you can use it.

- Define your interfaces with the highest possible option that will suffice. Don't use an `Activity` when a Context will do.

- If you're not building a replacement for the dialer, use `ACTION_DIAL` _not_ `ACTION_CALL` to initiate a call.

- Requesting updates from a system service may drain battery, so register for updates in onResume and unregister in onPause.

- Variable and `init` block declaration order in Kotlin, actually matters :) if you want to use a variable inside init {} initialize it before it.

- When comparing intents it does _not_ compare any extra data included in the intents [[Ref Link](<https://developer.android.com/reference/android/content/Intent#filterEquals(android.content.Intent)>)]

- To show a ringtone picker to the user, use the `ACTION_RINGTONE_PICKER` intent to launch the picker as a subactivity.

- Want to remove focusState on an item in GridView? Try: `android:listSelector="#00000000"`

- You can generate the **proguard** keep rules via the APK Analyzer inside Android Studio.

  ![proguard_rules_apk_analyzer](img/proguard_rules_apk_analyzer.gif)

- When viewing an Android Manifest, there is a tab at the bottom that allows you to see the merged manifest. Use this to inspect the merged manifest and find conflicts. [[Ref Link](https://developer.android.com/build/manage-manifests#inspect_the_merged_manifest_and_find_conflicts)]

  ![manifest-merged](img/manifest-merged.png)

- In the APK analyzer in Android Studio, classes/members listed in italic are only references, not definitions. If it's in italics, it's defined in another DEX file (or the SDK).

  ![apk_analyzer_ref](img/apk_analyzer_ref.jpeg)

- To be able to write multiline Todo comments, simply indent by 1 tab from second line onwards.

  ![multiline_todo_comment](img/multiline_todo_comment.png)

- You can get rid of a lot of noise in the Logcat, by Right Clicking a selected text > "Fold lines like this" option!.

  ![fold_line_like_this](img/fold_line_like_this.gif)

- You know how you can group ur code inside IDEs such as Android Studio and IntelliJ IDEA by using the `region` and `endregion` comment blocks. Turns out you can use the same trick to group inside XML files such as for layout, strings, styles, colors xml files
  
    ![region_cmt](img/region_cmt.gif)

- How many of you have had issue with special characters (&,<, >, etc) in your strings.xml file? Did you know there is an action called "Encode XML/HTML Special Characters" inside Android Studio that can escape those characters for you!

    ![encode_special_1](img/encode_special_1.gif)

    - The option is also avaliable under **Edit menu** drop down

        ![encode_special_2](img/encode_special_2.png)

    - In case the issue is in just one line, you can also just `ALT+ENTER` to get contextual fix.

        ![encode_special_3](img/encode_special_3.png)