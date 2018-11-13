
from general import *#toolbox.
InventoryOrigin = (441,328)#top left slot 440/328
OfferOrigin = (41,115)


def toggleInventory():
    tap('i')

def moveToSlot(x,y, move = True):#x ranges from 1-12, y ranges from 1-5
    centerCursor()
    add = 0
    if(x >= 2):
        add += 1
    if(x >= 6):
        add += 1
    if (x >= 10):
        add += 1
    xSlot = (x*29) + InventoryOrigin[0] + add
    ySlot = (y*29) + InventoryOrigin[1]
    if (move):
        mouse.move(xSlot,ySlot)#(((x*29)+440), (((y*29)+327))
    return mouse.position
#moveToSlot(0,0)
# - - -
def moveToOfferSlot(x,y,move = True):
    centerCursor()
    add = 0
    if(x >= 3):
        add += 1
    if (x >= 7):
        add += 1
    if (x >= 11):
        add += 1
    xSlot = (x*29) + OfferOrigin[0] + add
    ySlot = (y*29) + OfferOrigin[1]
    if (move):
        mouse.move(xSlot,ySlot)
    return mouse.position # returns the new mouse pos after centering and moving


def pickupItem(x,y):
    moveToSlot(x,y)
    leftClick()
    centerCursor()

def moveItem(x1,y1,x2,y2):# I can't think of any uses for this, we will always just be moving items from invetory to stash or to trade window
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
