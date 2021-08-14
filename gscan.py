import platform
import time
import threading
import subprocess
import sys

ASCII_ART = """
 ██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝ ██╔════╝██╔════╝██╔══██╗████╗  ██║
██║  ███╗███████╗██║     ███████║██╔██╗ ██║
██║   ██║╚════██║██║     ██╔══██║██║╚██╗██║
╚██████╔╝███████║╚██████╗██║  ██║██║ ╚████║
 ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

# Normally you wouldn't handle dependencies here...
try:
    from pynput import keyboard
    import pyautogui
except ImportError:
    input("Some dependencies are missing. Automatically install them?\n"
                "(press any key to install, CTRL+C or CTRL+BREAK/PAUSE to quit)")
    print("Installing missing dependencies...\n")
    subprocess.check_call([sys.executable, "-m", "pip", "install",
                           "pynput", "pyautogui"])
    print("\nFinished installing missing dependencies.\n")
finally:
    try:
        from pynput import keyboard
        import pyautogui
    except ImportError:
        print("\nDependencies not installed. Exiting.")
        sys.exit()


def determine_os():
    """
    Check which operating system user is running and display appropriate
    instructions.
    """

    if platform.system() == 'Windows':
        print('Press F7 to start, F8 to pause, CTRL+PAUSE/BREAK to quit.')
    else:
        print('Press F7 to start, F8 to pause, CTRL+C to quit.')

def start_scanning():
    """Press the WRITE_KEY every SLEEP_TIME seconds"""
    while SCAN_RUNNING:
        # For some reason pyautogui.press() doesn't play nice with the EVE
        # client so the following are used instead
        pyautogui.keyDown(WRITE_KEY)
        pyautogui.keyUp(WRITE_KEY)
        time.sleep(SLEEP_TIME)

def on_press(key):
    """Check which key is being pressed and either start or pause"""
    global SCAN_RUNNING
    # Change 'f7' to whichever key you want to start
    if key == keyboard.Key.f7 and not SCAN_RUNNING:
        SCAN_RUNNING = True
        t = threading.Thread(target=start_scanning)
        print('\nGScan running')
        t.start()
    # Change 'f8' to whichever key you want to stop
    elif key == keyboard.Key.f8:
        print('\nGScan paused')
        SCAN_RUNNING = False
        
if __name__ == '__main__':
    SCAN_RUNNING = False

    # Disable pyautogui failsafe
    pyautogui.FAILSAFE = False

    # Find OS and display instructions
    print(ASCII_ART)
    determine_os()

    # Edit these to change key/frequency
    SLEEP_TIME = 3
    WRITE_KEY = 'v'

    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print('\nClosing GScan...')
        sys.exit()
