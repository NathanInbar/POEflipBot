from pynput.keyboard import Key, Controller as kController, Listener
from pynput.mouse import Button, Controller as mController

import time, logging

keyboard = kController()
mouse = mController()
#  - - - - - -

def tap(key):
    keyboard.press(key)
    keyboard.release(key)

def centerCursor():
    mouse.position = (0,0)#this will try to set it to monitors 0,0 but POE windows locks the mouse so it will snap mouse to top left of the POE windows

def leftClick():
    mouse.press(Button.left)
    mouse.release(Button.left)
