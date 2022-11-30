from pynput.keyboard import Key,Controller
import time
def automation(parameter):
    keyboard = Controller()
    keyboard.press(Key.cmd_l)
    keyboard.release(Key.cmd_l)
    time.sleep(1)
    keyboard.type(parameter)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)