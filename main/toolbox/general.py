from pynput.keyboard import Key, Controller as kController, Listener
from pynput.mouse import Button, Controller as mController

import time, logging, os, sys

keyboard = kController()
mouse = mController()

league = 'Delve'
version = '0.0.0'

id_dictionary = {# to lookup the name of an ID you use id_dictionary[KEY] <- key being the ID
#This will just return the name of the 'looked' up ID
#id_dictionary[4] returns 'Chaos Orb'
-1 : "None",
1 : "Alteration",
2 : "Fusing",
3 : "Alchemy",
4 : "Chaos Orb",
5 : "Gemcutters",
6 : "Exalted",
7 : "Chroma",
8 : "Jewellers",
9 : "Chance",
10 : "Chisel",
11 : "Scour",
12 : "Blessed",
13 : "Regret",
14 : "Regal",
15 : "Divine",
16 : "Vaal",
17 : "Wisdom Scroll",
18 : "Portal Scroll",
19 : "Armourer's",
20 : "Whetstone",
21 : "Glassblowers",
22 : "Transmute",
23 : "Augmentation",
24 : "Mirror",
45 : "White Sextant",
46 : "Yellow Sextant",
47 : "Red Sextant",
69 : "Annulment Orb",
29 : "Blank"
}
#  - - - - - -

def tap(key):
    keyboard.press(key)
    keyboard.release(key)

def centerCursor():
    mouse.position = (0,0)#this will try to set it to monitors 0,0 but POE windows locks the mouse so it will snap mouse to top left of the POE windows

def leftClick():
    mouse.press(Button.left)
    mouse.release(Button.left)


# - - - - -
def getProjectPath():
    cwd = os.getcwd()
    cwd = cwd.replace("\\main\\toolbox", "")
    return cwd

def getResourcePath():
    return getProjectPath() + "\\resources"

def getMainResourcePath():
    return getProjectPath() + "\\main\\resources"
