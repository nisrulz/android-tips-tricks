# Setup ADB Aliases

**Setup handy `adb` aliases for your terminal** [[Ref Link]](https://medium.com/@jonfhancock/bash-your-way-to-better-android-development-1169bc3e0424#.8zcc4m5ch)

  Append the below **Aliases** to your `~/.bashrc` or `~/.zshrc` file, save and restart the terminal. Once saved, use them as show in **Usage** column

  ```bash
  # Take a screenshot
  # Usage: screenshot
  alias screenshot="adb exec-out screencap -p > screen-$(date -j "+%s").png"

  # Fire an intent
  # Usage: startintent https://twitter.com/nisrulz
  alias startintent="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X shell am start $1"

  # Install Apk
  # Usage: apkinstall ~/path/to/apk/App.apk
  alias apkinstall="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X install -r $1"

  # Uninstall an app
  # Usage: rmapp com.example.demoapp
  alias rmapp="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X uninstall $1"

  # Clear all data of an app
  # Usage: clearapp com.example.demoapp
  alias clearapp="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X shell pm clear $1"

  # Launch your debug apk on your connected device
  # Execute at the root of your android project
  # Usage: launchDebugApk
  alias launchDebugApk="adb shell monkey -p `aapt dump badging ./app/build/outputs/apk/debug/app-debug.apk | grep -e 'package: name' | cut -d \' -f 2` 1"
  ```
