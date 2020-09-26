from pynput import keyboard
import pyautogui
import threading
import time

# Edit these two to change key/frequency
SLEEP_TIME = 3
WRITE_KEY = 'v'

SCAN_RUNNING = False

print('Press F7 to start, F8 to stop.')

def start_scanning():
    global SCAN_RUNNING
    SCAN_RUNNING = True

    while SCAN_RUNNING:
        # For some reason pyautogui.press()
        # doesn't play nice with the EVE
        # client so the following are used instead
        pyautogui.keyDown(WRITE_KEY)
        pyautogui.keyUp(WRITE_KEY)
        time.sleep(SLEEP_TIME)

def on_press(key):
    global SCAN_RUNNING
    # Change 'f7' to whichever key you want to start
    if key == keyboard.Key.f7 and not SCAN_RUNNING:
        t = threading.Thread(target=start_scanning)
        print('GScan running')
        t.start()
    # Change 'f8' to whichever key you want to stop
    elif key == keyboard.Key.f8:
        print('GScan paused')
        SCAN_RUNNING = False
        
try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    print('Closing GScan...')
