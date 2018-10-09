from toolbox.general import *

InventoryOrigin = (422,302)#top left slot 440/327

def toggleInventory():
    tap('i')

def moveToSlot(x,y):#x ranges from 1-12, y ranges from 1-5
    xSlot = (x*29) + InventoryOrigin[0]
    ySlot = (y*29) + InventoryOrigin[1]
    mouse.move(xSlot,ySlot)#(((x*29)+440), (((y*29)+327))
# - - -
def pickupItem(x,y):
    moveToSlot(x,y)
    leftClick()
    centerCursor()

def moveItem(x1,y1,x2,y2):
    pickupItem(x1,y1)
    time.sleep(0.3)
    moveToSlot(x2,y2)
    time.sleep(0.3)
    leftClick()
    centerCursor()

def moveItemFast(x,y):
    moveToSlot(x,y)
    time.sleep(0.3)
    keyboard.press(Key.ctrl)
    time.sleep(0.3)
    leftClick()
    keyboard.release(Key.ctrl)
    time.sleep(0.3)
    centerCursor()
