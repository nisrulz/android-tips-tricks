![Image](https://github.com/nisrulz/android-tips-tricks/blob/master/img/github_banner.png)

### Featured in
[![Android Weekly](https://img.shields.io/badge/Android%20Weekly-%23221-blue.svg)](http://androidweekly.net/issues/issue-221)

Cheatsheet about tips and tricks for Android Development

This is a simple set of tips and tricks regarding Android Development which I have gathered from various sources. It helps me direct other android devs in my community regarding stuff each android dev should know about. Its also there for me to keep track of anything I either learn on my own or from other sources now and then when browsing the internet.

Contributions are always welcome, hoping people will help me in growing this. To contribute, simply open up a PR with the changes.

###***Know Your Tools***

####***Android Studio***

+ **Code faster by using keyboard shortcuts**
  
  |Description|Mac|Linux/Win
  |---|---|---
  |Lookup IDE commands|`Cmd`+`Shift`+`A`|`Ctrl`+`Shift`+`A`
  |Open Class|`Cmd`+`O`|`Ctrl`+`O`
  |Open File|`Cmd`+`Shift`+`O`|`Ctrl`+`Shift`+`N`
  |Open recently edited file|`Cmd`+`Shift`+`E`|`Ctrl`+`Shift`+`E`
  |Lookup Actions|`Cmd`+`Shift`+`A`|`Ctrl`+`Shift`+`A`
  |Open Symbol|`Cmd`+`Opt`+`O`|`Alt`+`Shift`+`N`
  |Open recently used file|`Cmd`+`E`|`Ctrl`+`E`
  |Last Edited Location|`Cmd`+`Shift`+`Backspace`|`Ctrl`+`Shift`+`Backspace`
  |Find Usage in persistent window|`Opt`+`F7`|`Alt`+`F7`
  |Find Usage in floating window|`Cmd`+`Opt`+`F7`|`Ctrl`+`Alt`+`F7`
  |Format the code with proper Indentation|`Cmd`+`Opt`+`L`|`Ctrl`+`Alt`+`L`
  |Surround With|`Opt`+`Cmd`+`T`|`Alt`+`Ctrl`+`T`
  |Open Terminal|`Opt`+`F12`|`Alt`+`F12`
  |Generate Setter/Getters/|`Cmd`+`N`|`Alt`+`Ins`
  |Find Class|`CMD`+`O`|`Ctrl`+`N`
  |Refactor/Rename|`Shift`+`F6`|`Shift`+`F6`
  |Quick Fix|`Opt`+`Enter`|`Alt`+`Enter`
  |Goto Definition|`Cmd`+`B`|`Ctrl`+`B`
  |Show parameters for selected method|`Cmd`+`P`|`Ctrl`+`P`
  |Refactor This|`Ctrl`+`T`|`Ctrl`+`Alt`+`Shift`+`T`
  |Stop Process|`Cmd`+`F2`|`Ctrl`+`F2`
  |Search Everywhere|`Shift`+`Shift`|`Shift`+`Shift`
  |Select Methods to Override|`Ctrl`+`O`|`Ctrl`+`O`
  |Delete Line|`Cmd`+`Backspace`|`Ctrl`+`Y`
  |Duplicate Line|`Cmd`+`D`|`Ctrl`+`D`

  **Complete Keymap Guide :  [MacOSX](https://resources.jetbrains.com/assets/products/intellij-idea/IntelliJIDEA_ReferenceCard_mac.pdf) | [Linux/Win](https://resources.jetbrains.com/assets/products/intellij-idea/IntelliJIDEA_ReferenceCard.pdf)**

+ **Use plugins to become more efficient**
  1. [KeyPromoter](https://plugins.jetbrains.com/plugin/4455)
  
    The plugin basically will annoy the hell out of you by showing you a big screen overlay with the key combination you should have used , if you used your mouse to execute some command to a level when you basically would start using the key combination just to avoid KeyPromoter annoying you all the time. 
    Its also is useful features, like it will prompt you to create a key binding for a command which does not have a key binding and you have used it 3 times.
  1. [String Manipulation](https://plugins.jetbrains.com/plugin/2162)

    Provides actions for text manipulation such as Toggle case, encode/decode, sorting, 
  1. [Lines Sorter](https://plugins.jetbrains.com/plugin/5919)

    Add Sort Lines action in Edit menu to sort selected lines or whole file if selection is empty.
  1. [Findbugs](https://plugins.jetbrains.com/plugin/3847?pr=idea) 

    Provides static byte code analysis to look for bugs in Java code from within Android Studio
  1. [Sonar Lint](https://plugins.jetbrains.com/plugin/7973) 

    Plugin that provides on-the-fly feedback to developers on new bugs and quality issues injected into Java, JavaScript and PHP code.
  1. [Checkstyles](https://plugins.jetbrains.com/plugin/1065) 

    Plugin provides both real-time and on-demand scanning of Java files from within Android Studio.

+ **Use Live Templates in Android Studio**
  + `logd` - Generates `Log.d(TAG, "");`
  + `newInstance` - Generates the static `newInstance` function inside a Fragment
  + `Toast` - Generates `Toast.makeText(context, "", Toast.LENGTH_SHORT).show();`

+ **Use the Darcula Theme in Android Studio**
Ok, I know its more like a preference , but trust me using that keeps your eyes less strained as they would be if you used the Default Light theme.

+ **Don't use a small font**
Preferably use a font in Android Studio thats easy to read and is at a font size which doesnot forces you to strain your eyes.
I use [Menlo font](https://en.wikipedia.org/wiki/Menlo_(typeface)).

+ **Use a code style**
You should use a standard codestyle 
 So possible contenders can be
  + [AOSP Codestyle](https://source.android.com/source/code-style.html)
  + [Square IntelliJ Codestyle](https://github.com/square/java-code-styles)
+ **Use the [Embedded Terminal inside Android Studio](https://www.jetbrains.com/help/idea/2016.2/working-with-embedded-local-terminal.html)**
+ **Use the Memory/Network/CPU Monitor inside Android Studio to profile your code/app**

####***Emulator***
Apart from using physical devices , one should use emulators as they are as of now easy to manage and equivalently powerful.

+ [Genymotion](https://www.genymotion.com/)
+ [Intel Emulator bundled in SDK Manger](https://developer.android.com/studio/run/emulator.html)

####***[Vysor](http://www.vysor.io/)***
This one needs special mention due to how useful it is. It basically is a window to your device i.e it streams and allows you to interact with your physical device on your laptop. Very useful when you are demo-ing your app during a presentation. You can interact with your physical device and it will be shown right in your laptop screen. It has a paid/free version , paid version is totally worth buying. 


-
###***Make better choices while coding***

+ **Use OkHttp over HttpUrlConnect**
HttpUrlConnect suffers from [quite some bugs](https://android-developers.blogspot.in/2011/09/androids-http-clients.html). 
[Okhttp](https://square.github.io/okhttp/) solves them in a more elegant manner. 
[[Reference Link]](https://corner.squareup.com/2013/05/announcing-okhttp.html)


+ **Reference local `aar` files as below [[Stackoverflow Ref](http://stackoverflow.com/a/28816265/2745762)]**
  ```gradle
    dependencies {
       compile(name:'nameOfYourAARFileWithoutExtension', ext:'aar')
     }
    repositories{
          flatDir{
                  dirs 'libs'
           }
     }

  ```

+ **Use [Pidcat](https://github.com/JakeWharton/pidcat) for logging**

+ **Use some Version Control System(VCS) like [Git](https://git-scm.com/)**

+ **Use [ClassyShark](https://github.com/google/android-classyshark)**
Its a standalone tool for Android Devs used to browse any Android executable and show important info such as class interfaces and members, dex counts and dependencies

+ **Use [Stetho](https://github.com/facebook/stetho)**
Debug your android apps using Chrome Dev Tools.

+ **Use [Battery Historian](https://github.com/google/battery-historian)**
A tool to analyze battery consumers using Android "bugreport" files.

+ **Always use a constant version value like "24.1.1"**
  Avoid using `+` when specifying the version of dependencies.
  + Keeps one secured from unexpected API changes in the dependency.
  + Avoids doing an extra network call for the checking latest version of each dependency on every build.

+ **Use [Handler instead of a TimerTask](http://www.mopri.de/2010/timertask-bad-do-it-the-android-way-use-a-handler/)**
+ **[Do not use your own personal email for Google Play Developer Account](https://www.reddit.com/r/Android/comments/2hywu9/google_play_only_one_strike_is_needed_to_ruin_you/)**
+ **Use Vectors instead of PNG**
  If you do **have** to use png, compress them. Take a look at [TinyPNG](https://tinypng.com).
+ **Use proguard**

  ```gradle
  android {
    ...
    buildTypes {
        release {
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}
  ```
+ **Use shrinkResources**

  ```gradle
  android {
    ...
    buildTypes {
        release {
            shrinkResources true
            minifyEnabled true
            ...
        }
    }
}
  ```

+ **[Simulating Android killing your app in the background](https://twitter.com/Jahnold/status/759775495655333888),  run in terminal**
  `adb shell am kill`

+ **Follow the below [rule to have faster gradle builds](https://medium.com/@skaliakoudas/decreasing-build-times-by-decreasing-gradle-memory-requirements-7fcafc6d98ea#.otnm0ofb6)**
  `Gradle memory >= Dex memory + 1Gb`

+ **Split your apk using gradle when using Native code, do not bundle all of em together and ship!.. coz that will make you evil**

  ```gradle
  defaultConfig {
      ...
  
      ndk {
        abiFilters "armeabi", "armeabi-v7a", "mips", "x86"
      }
    }
  
  //Split into platform dependent APK
    splits {
      abi {
        enable true
        reset()
        include 'armeabi', 'armeabi-v7a', 'mips', 'x86' //select ABIs to build APKs for
        universalApk false //generate an additional APK that contains all the ABIs
      }
    }
  
    // map for the version code
    project.ext.versionCodes = ['armeabi': 1, 'armeabi-v7a': 2, 'mips': 5, 'x86': 8]
  
    // Rename with proper versioning
    android.applicationVariants.all { variant ->
      // assign different version code for each output
      variant.outputs.each { output ->
        output.versionCodeOverride =
            project.ext.versionCodes.get(output.getFilter(com.android.build.OutputFile.ABI), 0) *
                1000000 +
                android.defaultConfig.versionCode
      }
    }
  ```

+ **Learn about some architecture such as MVP or Clean**

+ **Try to understand and follow TDD (Test Driven Development)**

+ **To force re-download of dependencies**

  ```gradle 
  ./gradlew --refresh-dependencies
  ```

+ **Follow the DRY principle**
DRY = Do not Repeat Yourself

+ **[Package by Feature, not layers](https://medium.com/the-engineering-team/package-by-features-not-layers-2d076df1964d)**

+ **[Learn about Dependency Resolution](http://crushingcode.co/the-curious-case-of-dependency-conflicts/)** 
  With the speed android dependencies update, sooner or later you are going to encounter some sort of dependency conflict. Solution is making use of Dependency Resoultion. [Official Reference](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.ResolutionStrategy.html)
  
+ **Use different package name for non-release builds**
  ```gradle
    android {
        buildTypes {
            debug {
                applicationIdSuffix '.debug'
                versionNameSuffix '-DEBUG'
            }

            release {
                // ...
            }
        }
    }
  ```


-

###***Tips regarding UI/UX***

+ **Points to note**
  + When implementing Ripple Effect use `?attr/selectableItemBackground` instead of `?android:attr` ([Ref](https://twitter.com/pareshmayani/status/772061422729637893))
  + When implementing Ripples contained within the view like Button, use `android:background="?attr/selectableItemBackground"` ([Ref](https://twitter.com/pareshmayani/status/772268888931176448))
  + When implementing Ripples that extend beyond the view's bounds like ImageView: `?attr/selectableItemBackgroundBorderless` ([Ref](https://twitter.com/pareshmayani/status/772269413290520576))

-

###***Other Resources***

+ **Listen to podcasts**
  1. [Fragmented](http://fragmentedpodcast.com/)
  2. [Android Developers Backstage](https://androidbackstage.blogspot.in/)

  There are others too, but the above two are the popular ones, you can lookup more using tag `android` on sites offering Podcast Services.

  P.S : I use [Player.fm](https://player.fm/) to listen to these podcasts. They even have an [Android Client](https://play.google.com/store/apps/details?id=fm.player&hl=en) , all for FREE.

+ **Checkout [CodePath Android Cliffnotes](https://guides.codepath.com/android)**

   It is the central crowdsourced resource for complete and up-to-date practical Android developer guides for any topic.

+ **Checkout new android libraries**

  [Android Arsenal](https://android-arsenal.com/) - Android developer portal with tools, libraries, and apps

+ **Checkout android example apps**
  + [Android Examples](https://github.com/nisrulz/android-examples) - Simple basic isolated apps, for budding android devs.
  + [Google Samples](https://github.com/googlesamples) - Various sample apps provided by Google

+ **Follow on Twitter**
  + [#AndroidDev](https://twitter.com/search?q=%23AndroidDev)

+ **Create a List on Twitter**
  + [Android List](https://twitter.com/nisrulz/lists/android)

+ **Bookmark these sites for staying upto date**
  + [Android Developers - Youtube Channel](https://www.youtube.com/user/androiddevelopers/videos)
  + [Android Niceties - UI Showcase](http://androidniceties.tumblr.com/)
  + [Material Design Specs](https://material.google.com/)
  + [Platform Version Distribution](https://developer.android.com/about/dashboards/index.html#Platform)
  + [Android Studio Release Notes](https://sites.google.com/a/android.com/tools/recent)
  + [Android Developers Blog](https://android-developers.blogspot.in/)
  + [AndroidDev-Reddit](https://www.reddit.com/r/androiddev)
  + [Github Trending Java Projects](https://github.com/trending?l=java&since=weekly)
  + [Stackoverflow-Android tag](https://stackoverflow.com/questions/tagged/android)
  + [Support Library History](https://developer.android.com/topic/libraries/support-library/revisions.html)
  + [Android Conferences](https://androidstudygroup.github.io/conferences/)
  + [Android Dev Docs](https://developer.android.com/reference/packages.html)
  + [Material Up - DesignShowcase](http://www.material.uplabs.com/)
  + [Dribbble - MaterialDeisgnShowcase](https://dribbble.com/tags/material_design)

+ **Use freely available mockable api points**
  + [Mockey](https://github.com/clafonta/Mockey) - A tool for testing application interactions over http, with a focus on testing web services, specifically web applications that consume XML, JSON, and HTML.
  + [JSON Placeholder](http://jsonplaceholder.typicode.com/) - Fake Online REST API for Testing and Prototyping
  + [API Studio](http://apistudio.io/) - a playground for API developers
  + [Mocky](http://www.mocky.io/) - Mock your HTTP responses to test your REST API
  + [Mockbin](http://mockbin.com) - Mockbin allows you to generate custom endpoints to test, mock, and track HTTP requests & responses between libraries, sockets and APIs.

+ **Subscribe to newsletters to stay upto date**
  + [Android Weekly](http://androidweekly.net/) - Free newsletter that helps you to stay cutting-edge with your Android Development
  + [AndroidDevDigest](https://www.androiddevdigest.com/) - A Handcrafted Weekly #AndroidDev Newsletter
  + [Infinium #AndroidSweets](https://androidsweets.ongoodbits.com/) - Fresh news from Droid zone
  + [Kotlin Weekly](http://us12.campaign-archive2.com/home/?u=f39692e245b94f7fb693b6d82&id=93b2272cb6) - Free newsletter to stay uptodate with Kotlin Development

+ **Some other awesome utility tools**
  + [Android SVG to VectorDrawable](https://inloop.github.io/svg2android/) - One VectorDrawable to rule all screen densities
  + [SQLite Viewer](https://inloop.github.io/sqlite-viewer/) - View sqlite file online
  + [Android 9-patch shadow generator](https://inloop.github.io/shadow4android/) - Tool that makes fully customizable shadows possible
  + [APK method count](https://inloop.github.io/apk-method-count/) - Tool that outputs per-package method counts
  + [Material Palette](https://www.materialpalette.com/) - Easily generate the color pallete based on material design
  + [Javadoc Themer](javadocthemer.crushingcode.co) - Give your boooring javadocs a splash of colors!
  + [Method Count](http://www.methodscount.com/) - Use this tool to avoid the dreaded 65K method limit of the DEX file format!
  + [Gradle, please](https://gradleplease.appspot.com/) - Lookup dependency reference name to include as your gradle dependencies
  + [jsonschema2pojo](http://www.jsonschema2pojo.org/) - Generate Plain Old Java Objects from JSON or JSON-Schema

-

#### **Extra : Android Libraries built by me**
+ [EasyDeviceInfo](https://github.com/nisrulz/easydeviceinfo) - Enabling device information to be at android developers hand like a piece of cake!
+ [Sensey](https://github.com/nisrulz/Sensey) - Android library to make detecting gestures easy
+ [PackageHunter](https://github.com/nisrulz/PackageHunter) - Android library to hunt down package information
+ [Zentone](https://github.com/nisrulz/zentone) - Easily generate audio tone in android
+ [RecyclerViewHelper](https://github.com/nisrulz/recyclerviewhelper) - RecyclerViewHelper provides the most common functions around recycler view like Swipe to dismiss, Drag and Drop, Divider in the ui, events for when item selected and when not selected, on-click listener for items.
+ [StackedHorizontalProgressbar](https://github.com/nisrulz/stackedhorizontalprogressbar) - Android Library to implement stacked horizontal progressbar
+ [QREader](https://github.com/nisrulz/qreader) - A library that uses google's mobile vision api and simplify the QR code reading process
+ [ScreenShott](https://github.com/nisrulz/screenshott) - Simple library to take a screenshot of the device screen , programmatically! 
+ [EvTrack](https://github.com/nisrulz/EvTrack) - Android library to make event and exception tracking easy
+ [OptimusHTTP](https://github.com/nisrulz/OptimusHTTP) - Android library that simplifys networking in android via an async http client
+ [ShoutOut](https://github.com/nisrulz/ShoutOut) - Android library for logging information in android


####Credits
This curated cheatsheet includes tips and tricks that I have been following in my workflow as well as those being suggested/followed by other android devs worldwide.I have tried to add direct links  wherever I could remember, giving people due credit who have explained the concepts. If  you think I have missed any , then either send a PR or open an issue and I will fix it asap.

License
=======

    Copyright 2016 Nishant Srivastava

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
