
"""
PoeFlipBot utilizes image recognition to verify the amount and type of each currency entering and exiting
each trade. This is crucial for the integrity and efficiency of the bot itself.
"""
from inventory import *
from general import *
import time, sys, random

cols = 12
rows = 5
read_delay = 0.01# Used for debug only. Set to 0 for practical application

currently_in_offer_window = []
"""
Basically, read part of screen (i.e: inventory, trade window, stash) and parse its currency type and quantity (white text top left))
Compare screencap to database of locally saved currency images. (loop through all, and take highest probability one)
"""
#Currency Icons (59x59) are stored in main/resources/PoE-Currency-Icons  each image corresponds to its Item ID according to readME
def checkSlot(x,y):#checks invetory slot
    slot_coords = moveToOfferSlot(x,y,True)#use the coordinates of each slot of imageRecognition

    #Do the logic here to detect what id and quant the item is.
    id = random.randrange(1,2) # TO-DO: LOGIC (with image recog)
    quant = random.randrange(1,11) # TO-DO: LOGIC (with image recog)
    slot_offer = (id,quant) # nicely packed tuple to pass as an arg
    #if the slot is blank we shouldn't append anything.
    
    currently_in_offer_window.append(  slot_offer  )#append what the checked slot is offering and append it.


def checkTradeWindow():#12x5 (12 columns, 5 rows)
    """Will check every slot in the trade window and log its type and amount"""
    for y in range(cols):
        for x in range(rows):
            checkSlot(y,x)#for every slot, read the ID and quant
            time.sleep(read_delay)#This time.sleep is to simulate reading time for the image recog

def sortOffered(offered,sort,first = True):
    if(first):
        for x in range(len(offered)):
            if (contains(sort,offered[x][0])):
                pass
            else:
                sort.append(   (offered[x][0],0)    )
    for y in range(len(sort)):
        for x in range(len(offered)):
            if (sort[y][0] == offered[x][0]):
                sort[y] = (sort[y][0], sort[y][1] + offered[x][1])
    print(sort)


def contains(check,value):#Checks if value is contained in iterable-type-list check
    for x in range (len(check)):
        if check[x][0] == value:
            return True
    return False

def checkOfferWithTrade(trade_expected, currently_offered):
    if(trade_expected[0][0] == currently_offered[0][0]):#if the id's are the same
        if (currently_offered[0][1] >= trade_expected[0][1]):
            return True#trade matches or better
    return False

def determineIfInTrade():#--
    """Scan some guarenteed pixels to see if in trade window or not"""
    pass

checkTradeWindow()
sortOffered(currently_in_offer_window,[])

"""
HOW TO USE imageRecognition
1) determineIfInTrade()  # if this returns True then you are in a trade window
2) --insert our trade items into trade window (not handled by imageRecognition)
3) Scan offered trades. checkTradeWindow() <---- this will go through every slot on the offered side of the trade window to verify ID and Quant
4) sortOffered() <--- nicely sorts all offered items into a list of tuples containing each ID and Quant being offered to us
5) Determine whether or not the offer matches our trade request. checkOfferWithTrade(trade_expected, currently_offered)
6) -- accept or deny trade with follow-up message (TY, or some error message sent to user) (not handled with imageRecognition)
7) -- Stash new items and log them (not handled by imageRecognition)
"""
