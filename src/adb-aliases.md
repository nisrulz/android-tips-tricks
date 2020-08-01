# Setup ADB Aliases

Append the below **Aliases** to your `~/.bashrc` or `~/.zshrc` file, save and restart the terminal. Once saved, use them as show in **Usage** column

```bash
#############################################################
# Android aliases + path
#############################################################

# Path to Android SDK (This is for Mac, replace for your OS)
export ANDROID_HOME=$HOME/Library/Android/sdk

# Path to NDK
export ANDROID_NDK_HOME=$ANDROID_HOME/ndk

# Path to Android platform tools (adb, fastboot, etc)
export ANDROID_PLATFORM_TOOLS="$ANDROID_HOME/platform-tools"

# Path to Android tools (monitor, mksdcard, emulator-check, emulator, etc)
export ANDROID_TOOLS_1="$ANDROID_HOME/tools"

# Path to Android tools (apkanalyzer, avdmanager, monkeyrunner, lint, sdkmanager etc)
export ANDROID_TOOLS_2="$ANDROID_HOME/tools/bin"

# Path to Android tools (aapt, apksigner, zipalign, etc)
export ANDROID_TOOLS_3="$ANDROID_HOME/build-tools/29.0.3/"

# Add all to the path
export PATH="$PATH:$ANDROID_PLATFORM_TOOLS:$ANDROID_TOOLS:$ANDROID_TOOLS_2:$ANDROID_TOOLS_3"

# Demo Mode : https://android.googlesource.com/platform/frameworks/base/+/master/packages/SystemUI/docs/demo_mode.md
# Enable Demo Mode on your device
# Usage: enableDemoMode
alias enableDemoMode="adb shell settings put global sysui_demo_allowed 1 && adb shell am broadcast -a com.android.systemui.demo -e command clock -e hhmm 1200 && adb shell am broadcast -a com.android.systemui.demo -e command network -e mobile show -e level 4 -e datatype false && adb shell am broadcast -a com.android.systemui.demo -e command notifications -e visible false && adb shell am broadcast -a com.android.systemui.demo -e command battery -e plugged false -e level 100"

# Disable Demo Mode on your device
# Usage: disableDemoMode
alias disableDemoMode="adb shell am broadcast -a com.android.systemui.demo -e command exit"

# Install and Grant all permissions for an apk
# Usage: grantAllPermissionsForApk path/to/apk/Application.apk
alias grantAllPermissionsForApk="adb install -g $1"

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

# Get package name of the passed apk file
# Usage: getPackageName app-debug.apk
alias getPackageName="apkanalyzer -h manifest application-id $1"

# Stress test the debug apk with 100000 ui events
# Execute at the root of your android project
# Use as: stressTestDebugApk apk_file.apk
function stressTestApk() {
    local APP_PACKAGE_NAME=$(getPackageName $1)
    adb shell monkey -p $APP_PACKAGE_NAME 100000
}

# Install APK to device
# Use as: apkinstall app-debug.apk
alias apkinstall="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X install -r $1"

# As an alternative to apkinstall, you can also do just ./gradlew installDebug
# Alias for building and installing the apk to connected device
# Use as: buildAndInstallApk path/to/apk_file.apk
# Example: To build and install debug apk
#        > buildAndInstallApk  ./app/build/outputs/apk/debug/app-debug.apk
alias buildAndInstallApk="./gradlew assembleDebug && apkinstall $1"

# Launch your apk on your connected device
# Execute at the root of your android project
# Usage: launchApk path/to/apk_file.apk
# Example: To launch debug apk
#        > launchApk  ./app/build/outputs/apk/debug/app-debug.apk
alias launchApk="adb shell monkey -p $(getPackageName $1) 1"

# ------------- Single command to build+install+launch apk------------#
# Execute at the root of your android project
# Use as: buildInstallLaunchApk path/to/apk_file.apk
# Example: To build, install and launch debug apk
#        > buildInstallLaunchApk  ./app/build/outputs/apk/debug/app-debug.apk
alias buildInstallLaunchApk="buildAndInstallApk $1 && launchDebugApk $1"
```
