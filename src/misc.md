# Misc

### **_Other Resources_**

- [Google's Maven Repository](https://dl.google.com/dl/android/maven2/index.html)

- **[Take care about copyright](http://jeroenmols.com/blog/2016/08/03/copyright/)**

- **Checkout new android libraries**

  [Android Arsenal](https://android-arsenal.com/) - Android developer portal with tools, libraries, and apps

- **Follow on Twitter**

  - [#AndroidDev](https://twitter.com/search?q=%23AndroidDev)

- **Create a List on Twitter**

  - [Android List](https://twitter.com/nisrulz/lists/android)

- **Fix issue with Audio getting worse on your Bluetooth Headset when starting Emulator**

  You can deal with this problem in 2 ways.
  1. Using Terminal

    ```sh
    # i.e emulator -noaudio-avd Pixel_4a_API_31
    emulator -noaudio-avd <emulator_name>
    ```

  2. Editing the config for Emulator

    Navigate to your existing Emulator and edit the `config.ini` file
    
    ```sh
    # Wipe Data + Cold Boot once
    hw.audioInput = no
    hw. audioOutput = no
    ```
    Read an indepth article [here](https://blog.mmckenna.me/android-emulators-vs-bluetooth-headphones)
