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
The plugin basically will annoy the hell out of you by showing you a big screen overlay with the key combination you should have used , if you used your mouse to execute some command to a level when you basically would start using the key combination just to avoid KeyPromoter annoying you all the time. 

Its also is usefull features, like it will prompt you to create a key binding for a command which does not have a key binding and you have used it 3 times.

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
