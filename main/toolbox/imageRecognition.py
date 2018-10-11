
"""
PoeFlipBot utilizes image recognition to verify the amount and type of each currency entering and exiting
each trade. This is crucial for the integrity and efficiency of the bot itself.
"""
from toolbox.inventory import *
from toolbox.general import *

"""
Basically, read part of screen (i.e: inventory, trade window, stash) and parse its currency type and quantity (white text top left))
Compare screencap to database of locally saved currency images. (loop through all, and take highest probability one)
"""
#Currency Icons (59x59) are stored in main/resources/PoE-Currency-Icons  each image corresponds to its Item ID according to readME
def checkSlot(x,y):#checks invetory slot
    slot_coords = moveToSlot(x,y,False)# made a tweak to inventory.moveToSlot() by adding a default arg and a return statement.
    print(slot_coords)
