from toolbox.general import *

InventoryOrigin = (440,327)#top left slot

def toggleInventory():
    tap('i')

def moveToSlot(x,y):#x ranges from 1-12, y ranges from 1-5
    xSlot = (x*29) + InventoryOrigin[0]
    ySlot = (y*29) + InventoryOrigin[1]
    mouse.move(xSlot,ySlot)#(((x*29)+440), (((y*29)+327))
