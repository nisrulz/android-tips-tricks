# [scrcpy](https://github.com/genymobile/scrcpy)

It is basically used to display and control your Android device and is the open source equivalent of [Vysor](http://www.vysor.io/). The good folks at [Genymotion](https://www.genymotion.com/) built this tool and then open sourced it (Open Source FTW).

# How to Use Scrcpy to Mirror and Control Your Android Device

Scrcpy (short for "screen copy") is a free and open-source tool that allows you to mirror and control an Android device from your computer. It's a useful tool for various purposes, including presentations, debugging, or simply using your Android device on a larger screen. Here's how to use scrcpy:

## Prerequisites

Before you start, ensure that you have Android Debug Bridge (ADB) set up on your computer, as scrcpy relies on ADB for device communication.

1. **Download and Install Scrcpy:**

   - You can download scrcpy from the official GitHub repository: [Scrcpy Releases](https://github.com/Genymobile/scrcpy/releases)
   - Download the appropriate version for your operating system (Windows, macOS, or Linux).

2. **Connect Your Android Device:**

   - Enable Developer Options on your Android device by going to "Settings" > "About phone" > "Software information" > tap on "Build number" seven times.
   - Once Developer Options are enabled, go to "Developer Options" (usually found under "System" or "About phone").
   - Enable "USB debugging."
   - Connect your Android device to your computer using a USB cable. Make sure USB debugging is enabled before connecting.

3. **Run Scrcpy:**

   - Open a command prompt or terminal window on your computer.
   - Navigate to the directory where you downloaded scrcpy.
   - Run the following command to start scrcpy:

     ```bash
     scrcpy
     ```

   - Scrcpy should detect your connected Android device and mirror its screen to your computer.

4. **Control Your Android Device:**

   - You can now interact with your Android device using your computer's mouse and keyboard.
   - To switch between fullscreen and windowed mode, press `Ctrl` + `f`.
   - To rotate the screen (if needed), press `Ctrl` + `r`.

5. **Using Scrcpy Options:**

   - Scrcpy has various command-line options you can use to customize the experience. For example, you can adjust the resolution, change the bit rate, or enable/disable screen recording. You can find a list of these options in the scrcpy documentation: [Scrcpy Command Line Usage](https://github.com/Genymobile/scrcpy#command-line-usage)

6. **Quit Scrcpy:**

   - To exit scrcpy, simply close the terminal or command prompt window running scrcpy.

Scrcpy is a powerful tool for mirroring and controlling Android devices from your computer, and it's relatively straightforward to use once you have ADB set up.
