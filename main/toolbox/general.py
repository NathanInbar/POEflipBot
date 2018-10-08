from pynput.keyboard import Key, Controller, Listener
from pynput import mouse

import time, logging

keyboard = Controller()
mouse = mouse.Controller()
#  - - - - - -

def tap(key):
    keyboard.press(key)
    keyboard.release(key)

def centerCursor():
    mouse.position = (0,0)#this will try to set it to monitors 0,0 but POE windows locks the mouse so it will snap mouse to top left of the POE windows
