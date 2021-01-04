# GScanner
Simple script to automatically use directional scanner in the video game EVE Online. Very useful for wormhole living!
### Requirements
GScanner uses the <code>pyautogui</code> and <code>pynput</code> modules. They can be installed with the following command:  
```
pip install pyautogui pynput
```
### Instructions
Press F7 to start GScanner, F8 to pause, and CTRL+C to quit on Linux, CTRL+PAUSE/BREAK to quit on Windows.

### Recent Changes
- Rearranged order of <code>start_scanning</code> function to 'press' the key before waiting, rather than after, to avoid the key being pressed after users pause the script.
- Removed pyautogui's failsafe (it could potentially break the script if user moves their cursor to the corner of the screen too quickly while playing)

