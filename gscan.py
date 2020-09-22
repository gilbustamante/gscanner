from pynput import keyboard
import pyautogui
import threading
import time

#### ONLY EDIT THESE ####
SLEEP_TIME = 3
WRITE_KEY = 'v'
START_KEY = f7 
STOP_KEY = f8
#### ONLY EDIT THESE ####

SCAN_RUNNING = False

def start_scanning():
    global SCAN_RUNNING
    SCAN_RUNNING = True

    while SCAN_RUNNING:
        time.sleep(SLEEP_TIME)
        pyautogui.keyDown(WRITE_KEY)
        pyautogui.keyUp(WRITE_KEY)

def on_press(key):
    global SCAN_RUNNING
    # Change 'f7' to whichever key you want to start
    if key == keyboard.Key.f7 and not SCAN_RUNNING:
        t = threading.Thread(target=start_scanning)
        t.start()
    # Change 'f8' to whichever key you want to stop
    elif key == keyboard.Key.f8:
        SCAN_RUNNING = False
        
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
