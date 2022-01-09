# Setup Android Aliases

Append the below **Aliases** to your `~/.bashrc` or `~/.zshrc` file, save and restart the terminal. Once saved, use them as show in **Usage** column

```bash
#############################################################
# Setup Android Paths
#############################################################

# Path to Android SDK (This is for Mac, replace for your OS)
export ANDROID_HOME=$HOME/Library/Android/sdk

# Path to NDK
export ANDROID_NDK_HOME=$ANDROID_HOME/ndk/22.1.7171670

# Path to Android platform tools (adb, fastboot, etc)
export ANDROID_PLATFORM_TOOLS="$ANDROID_HOME/platform-tools"

# Path to Android tools (monitor, mksdcard, emulator-check, emulator, etc)
export ANDROID_TOOLS_1="$ANDROID_HOME/tools"

# Path to Android tools (apkanalyzer, avdmanager, monkeyrunner, lint, sdkmanager etc)
export ANDROID_TOOLS_2="$ANDROID_HOME/tools/bin"

# Path to Android tools (aapt, apksigner, zipalign, etc)
export ANDROID_TOOLS_3="$ANDROID_HOME/build-tools/29.0.3/"

# Path to Android tools (emulator)
export ANDROID_TOOLS_4="$ANDROID_HOME/emulator/"

# Add all to the path
export PATH="$PATH:$ANDROID_PLATFORM_TOOLS:$ANDROID_TOOLS:$ANDROID_TOOLS_2:$ANDROID_TOOLS_3:$ANDROID_TOOLS_4"

#############################################################
# Setup Android Aliases
#############################################################

# Do an incremental install of APK
# Usage: incrementalInstall
alias incrementalInstall="adb intall --fastdeploy"

# Alias to run local test while only showing failed tests as output
# Usage: runLocalTest
alias runLocalTest="./gradlew --rerun-tasks test | grep FAILED"

# Delete all build folders in an Android project
# Usage: deleteAllBuildDirs
alias deleteAllBuildDirs='find . -type d -name "build" \
    | while read f; do echo "🔥Deleting: $f" && rm -rf "$f"; done'

# Install and Grant all permissions for an apk
# Usage: grantAllPermissionsForApk path/to/apk/Application.apk
alias grantAllPermissionsForApk="adb install -g $1"

# Take a screenshot
# Usage: screenshot
alias screenshot="adb exec-out screencap -p > screen-$(date -j "+%s").png"

# Fire an intent
# Usage: startIntent https://twitter.com/nisrulz
alias startIntent="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X shell am start $1"

# Install Apk
# Note: As an alternative to apkInstall, you can also do just ./gradlew installDebug
# Usage: apkInstall ~/path/to/apk/App.apk
alias apkInstall="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X install -r $1"

# Uninstall an app
# Usage: rmApp com.example.demoapp
alias rmApp="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X uninstall $1"

# Clear all data of an app
# Usage: clearApp com.example.demoapp
alias clearApp="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X shell pm clear $1"

# Get package name of the passed apk file
# Usage: getPackageName app-debug.apk
alias getPackageName="apkanalyzer -h manifest application-id $1"

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

# Single command to build+install+launch apk
# Execute at the root of your android project
# Use as: buildInstallLaunchApk path/to/apk_file.apk
# Example: To build, install and launch debug apk
#        > buildInstallLaunchApk  ./app/build/outputs/apk/debug/app-debug.apk
alias buildInstallLaunchApk="buildAndInstallApk $1 && launchDebugApk $1"

# ------------- Demo Mode ------------#

# Demo Mode : https://android.googlesource.com/platform/frameworks/base/+/master/packages/SystemUI/docs/demo_mode.md

# Enable Demo Mode on your device
# Usage: enableDemoMode
alias enableDemoMode="adb shell settings put global sysui_demo_allowed 1 \
&& adb shell am broadcast \
-a com.android.systemui.demo -e command clock -e hhmm 1200 \
&& adb shell am broadcast \
-a com.android.systemui.demo -e command network \
-e mobile show -e level 4 -e datatype false \
&& adb shell am broadcast -a com.android.systemui.demo \
-e command notifications \
-e visible false && adb shell am broadcast \
-a com.android.systemui.demo -e command battery \
-e plugged false -e level 100"

# Disable Demo Mode on your device
# Usage: disableDemoMode
alias disableDemoMode="adb shell am broadcast -a com.android.systemui.demo -e command exit"

# ------------- Dev Mode:Layout Bounds ------------#

# Ref link: https://ivanmorgillo.com/2021/06/24/show-layout-bounds-from-command-line/
# Enable Layout Bounds developer options
# Usage: devLayoutBoundsOn
alias devLayoutBoundsOn='adb shell setprop debug.layout true; adb shell service call activity 1599295570 > /dev/null'

# Disable Layout Bounds developer options
# Usage: devLayoutBoundsOff
alias devLayoutBoundsOff='adb shell setprop debug.layout false ; adb shell service call activity 1599295570 > /dev/null'

#############################################################
# Setup Android Bash Functions
#############################################################

# Uninstall all installed apps from the connected device 
# whose package name matches the passed pattern
# Usage: uninstallAppsMatchingPackagePattern github.nisrulz.
function uninstallAppsMatchingPackagePattern(){
    echo ""
    # Break down of the long command
    # adb shell 'pm list packages -u'  = Get all packages
    # grep github.nisrulz              = Filter out the packages that contain value of $1 arg
    # cut -c 9-                        = Remove the first 9 chars, which correspond to package:
    # rev                              = Reverse the string
    # cut -c 2-                        = Remove the first 2 chars, which correspond to ^M
    # rev                              = Reverse the string
    for pkg in $(adb shell 'pm list packages -u' | grep $1 | cut -c 9- | rev | cut -c 2- | rev); do
        echo "-- Removing $pkg"
        adb uninstall $pkg
    done
}

# Usage: Navigate to the library directory and execute the below
#       > ndk_stack_tracing
function ndk_stack_tracing(){
    adb logcat | $ANDROID_NDK_HOME/ndk-stack -sym ./build/intermediates/library_jni/debug/jni/arm64-v8a/
}

# Stress test the debug apk with 100000 ui events
# Execute at the root of your android project
# Use as: stressTestApk apk_file.apk
function stressTestApk() {
    local APP_PACKAGE_NAME=$(getPackageName $1)
    adb shell monkey -p $APP_PACKAGE_NAME 100000
}

# Find the usage of OptIn annotation in codebase
# Usage: findOptInAnnotationUsage
function findOptInAnnotationUsage(){
    grep -r -F "@OptIn(" ./ 
}

# ADB Over Wifi
# Usage: adbOverWifi
function adbOverWifi() {
    local DEVICE_ID=$(adb devices | awk 'NR==2{print $1; exit}')
    echo "Device ID: $DEVICE_ID"

    local LOCAL_WIFI_IP=$(adb shell ip route | awk 'NR==1{print $9}')
    echo "Local Wifi IP: $LOCAL_WIFI_IP"

    local PORT=5555
    adb tcpip $PORT
    adb connect $LOCAL_WIFI_IP:$PORT
    sleep 1
    adb devices
}
```
