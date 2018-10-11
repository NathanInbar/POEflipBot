from toolbox.general import *
InventoryOrigin = (422,302)#top left slot 440/327

itemID = {
    1 : 'alteration',
    2 : 'fusing',
    3 : 'alchemy',
    4 : 'chaos',
    5 : 'gemcutters',
    6 : 'exalted',
    7 : 'chroma',
    8 : 'jewellers',
    9 : 'chance',
    10 : 'chisel',
    11 : 'scour',
    12 : 'blessed',
    13 : 'regret',
    14 : 'regal',
    15 : 'divine',
    16 : 'vaal',
    19 : 'armour',
    20 : 'whetstone',
    21 : 'glassblowers',
    22 : 'transmutes',
    23 : 'augmentation',
    24 : 'mirror',
}

def toggleInventory():
    tap('i')

def moveToSlot(x,y, move = True):#x ranges from 1-12, y ranges from 1-5
    xSlot = (x*29) + InventoryOrigin[0]
    ySlot = (y*29) + InventoryOrigin[1]
    if (move):
        mouse.move(xSlot,ySlot)#(((x*29)+440), (((y*29)+327))
    return (xSlot,ySlot)
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
