# Android Tips & Tricks

Cheatsheet about tips and tricks for Android Development

###***Know Your Tools***

####***Android Studio***

#####**Tip #1 - Code faster by using keyboard shortcuts**
|Description|Mac|Linux/Win
|---|---|---
|Open Class|`Cmd`+`O`|`Ctrl`+`O`
|Open File|`Cmd`+`Shift`+`O`|`Ctrl`+`Shift`+`N`
|Open Symbol|`Cmd`+`Opt`+`O`|`Alt`+`Shift`+`N`
|Open recently used file|`Cmd`+`E`|`Ctrl`+`E`
|Open recently edited file|`Cmd`+`Shift`+`E`|`Ctrl`+`Shift`+`E`
|Last Edited Location|`Cmd`+`Shift`+`Backspace`|`Ctrl`+`Shift`+`Backspace`
|Find Usage in persistent window|`Opt`+`F7`|`Alt`+`F7`
|Find Usage in floating window|`Cmd`+`Opt`+`F7`|`Ctrl`+`Alt`+`F7`
|Format the code with proper Indentation|`Cmd`+`Opt`+`L`|`Ctrl`+`Alt`+`L`
|Lookup Actions|`Cmd`+`Shift`+`A`|`Ctrl`+`Shift`+`A`
|Surround With|`Opt`+`Cmd`+`T`|`Alt`+`Ctrl`+`T`

#####**Tip #2 - Use plugins to become more efficient**
1. [KeyPromoter](https://plugins.jetbrains.com/plugin/4455)
    The plugin basically will annoy the hell out of you by showing you a big screen overlay with the key combination you should have used , if you used your mouse to execute some command to a level when you basically would start using the key combination just to avoid KeyPromoter annoying you all the time. 
    Its also is usefull features, like it will prompt you to create a key binding for a command which does not have a key binding and you have used it 3 times.

1. [String Manipulation](https://plugins.jetbrains.com/plugin/2162)
2. [Lines Sorter](https://plugins.jetbrains.com/plugin/5919)

#####**Tip #3 - Use the Darcula Theme in Android Studio**
Ok, I know its more like a preference , but trust me using that keeps your eyes less strained as they would be if you used the Default Light theme.

#####**Tip #4 - Don't use a small font**
Preferably use a font in Android Studio thats easy to read and is at a font size which doesnot forces you to strain your eyes.
I use Menlo font.

#####**Tip #5 - Use a code style**
You should use a standard codestyle 
 So possible contenders can be
 
+ [AOSP Codestyle](https://source.android.com/source/code-style.html)
+ [Square IntelliJ Codestyle](https://github.com/square/java-code-styles)

####***Emulator***
Apart from using physical devices , one should use emulators as they are as of now easy to manage and equivalently powerful.

+ [Genymotion](https://www.genymotion.com/)
+ [Intel Emulator bundled in SDK Manger](https://developer.android.com/studio/run/emulator.html)


---
###***Make better choices while coding***

#### **Tip #1 - Use OkHttp over HttpUrlConnect**
HttpUrlConnect suffers from [quite some bugs](https://android-developers.blogspot.in/2011/09/androids-http-clients.html). 
[Okhttp](https://square.github.io/okhttp/) solves them in a more elegant manner. [[Ref]](https://corner.squareup.com/2013/05/announcing-okhttp.html)

#### **Tip #2 - Use [Pidcat](https://github.com/JakeWharton/pidcat) for logging**

#### **Tip #3 - Use the [Embedded Terminal inside Android Studio](https://www.jetbrains.com/help/idea/2016.2/working-with-embedded-local-terminal.html)**

#### **Tip #4 - Use git**

#### **Tip #5 - Use [ClassyShark](https://github.com/google/android-classyshark)**
Its a standalone tool for Android Devs used to browse any Android executable and show important info such as class interfaces and members, dex counts and dependencies

#### **Tip #6 - Use [ClassyShark](https://github.com/google/android-classyshark)**

#### **Tip #7 - Use [Stetho](https://github.com/facebook/stetho)**
Debug your android apps using Chrome Dev Tools.

#### **Tip #8 - Use [Battery Historian](https://github.com/google/battery-historian)**
A tool to analyze battery consumers using Android "bugreport" files.

#### **Tip #9 - Always use a constant version value like "24.1.1"**
Avoid using `+` when specifying the version of dependencies.

+ Keeps one secured from unexpected API changes in the dependency.
+ Avoids doing an extra network call for the checking latest version of each dependency on every build.

#### **Tip #10 - Use [Handler instead of a TimerTask](http://www.mopri.de/2010/timertask-bad-do-it-the-android-way-use-a-handler/)**

#### **Tip #11 - Split your apk using gradle when using Native code, donot bundle all of em together and ship!.. coz that will make you evil**

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

---
###***Other Resources***

#### **Tip #1 - Listen to podcasts**
1. [Fragmented](http://fragmentedpodcast.com/)
2. [Android Developers Backstage](https://androidbackstage.blogspot.in/)

P.S : I use [Player.fm](https://player.fm/) to listen to these podcasts. They even have an [Android Client](https://play.google.com/store/apps/details?id=fm.player&hl=en) , all for FREE.

#### **Tip #2 - Checkout new android libraries**
[Android Arsenal](https://android-arsenal.com/)


#### **Tip #3 - Use freely available mockable api points**
+ [Mockey](https://github.com/clafonta/Mockey) - A tool for testing application interactions over http, with a focus on testing web services, specifically web applications that consume XML, JSON, and HTML.
+ [JSON Placeholder](http://jsonplaceholder.typicode.com/) - Fake Online REST API for Testing and Prototyping
+ [API Studio](http://apistudio.io/) - a playground for API developers
+ [Mocky](http://www.mocky.io/) - Mock your HTTP responses to test your REST API
+ [Mockbin](http://mockbin.com) - Mockbin allows you to generate custom endpoints to test, mock, and track HTTP requests & responses between libraries, sockets and APIs.

---
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
