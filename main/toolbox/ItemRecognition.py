import time, sys, random, math
import numpy as np
#from skimage.measure import structural_similarity as ssim
import pyautogui
import imutils
import cv2
from inventory import *#toolbox.
from general import *#toolbox.
import glob
import clipboard as cb
#Size of inventory (trade window as well)
cols = 12
rows = 5
#---
#DEFAULTS
currently_in_offer_window = []
offer = []
initial_amount = -1;
amount_expected = -1
name_expected = ' '
should_copy = True;
#----
#----!!!!These two lines shouldn't really be in this file. origin should be stored on program startup and fed to this file from another.
centerCursor()
origin = mouse.position
#---

def checkSlot(x,y):
    global amount_expected
    """
    Will check the item on the mouse cursor and detect the Type and Quantity
    """
    moveToOfferSlot(x,y,True)
    if(should_copy):#only get item info if we need to
        info = getItemInfo()

        id = info[0]#Gets the info of the item on our cursor
        quantity = info[1]#Gets the info of the item on our cursor

        print("ID: {} : QT: {}".format(id,quantity) )

        slot_offer = (id,quantity)
        if(quantity > 0):
            amount_expected -= quantity#as we get more currency subtract, how much we are expecting.
            currently_in_offer_window.append(  slot_offer  )# what the checked slot is offering and append it.


def getTradeContents(expected_name,expected_quantity):
    global amount_expected
    global should_copy
    global name_expected
    global initial_amount
    amount_expected = expected_quantity
    initial_amount = expected_quantity
    name_expected = expected_name
    """
    checks each trade slot
    """
    for y in range(cols):
        for x in range(rows):
            checkSlot(y,x)
            if(amount_expected <= 0):
                should_copy = False;
                #print("we have enuf currency!!!")
                if(checkAllItemsHovered() == True):
                    sortOffered()
                    return

    sortOffered()

def sortOffered(offered = currently_in_offer_window, sort = [], first = True):
    """
    Sorts the list of currency in the trade offer window and returns True or False on whether or not we should
    take the trade.
    """
    global offer
    global name_expected
    global amount_expected
    global initial_amount
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
    print('Currently Offered Currency: {}'.format(sort))
    offer = sort
    print('Name_ex: {} and Quant_ex: {}'.format(name_expected,initial_amount))
    for y in range(len(offer)):
        for x in range(len(offer[0])):
            if(offer[y][0] == name_expected):
                if(offer[y][1] == initial_amount):
                    print("Accept Trade!")
                    acceptTrade()
                    return
    print('Decline Trade!')#We will continuosly rescan until the correct currency and quantity is inserted

def getOffer():
    return offer
def contains(check,value):#Checks if value is contained in iterable-type-list check
    for x in range (len(check)):
        if check[x][0] == value:
            return True
    return False
def acceptTrade():
    """
    Navigates mouse to ACCEPT button and clicks it.
    """
    centerCursor()
    mouse.move(105,460)#where the accept button is (also the same pixel that we are scanning to see if items are hovered)
    leftClick()#general function
def checkAllItemsHovered():
    accept_grab = pyautogui.screenshot(region = (origin[0] + 105,origin[1] + 460,1,1 ))
    accept_grab = cv2.cvtColor(np.array(accept_grab), cv2.COLOR_RGB2BGR)#COLOR_RGB2GRAY

    if(accept_grab[0][0][2] < 23):
        #not all items are hovered because the accept button isnt red
        return False;
        #now we mouse over each slot and take it as extra currency, strictly.
    print('all items hovered')
    return True

def checkTradeComplication():
    """
    This will check if a user has removed or inserted an item into the window.
    Checking for red-border that pops up when this occurs.
    When we do encounter a trade 'complication' we will stop all checking and reset and rescan window
    """
    #position of pixel in red-border (x,y)
    pass

def getItemInfo():
    """
    Gets the info of the item on our cursor and returns it to the checkSlot func
    """
    time.sleep(.1)
    copy()
    time.sleep(.1)
    return parseInfo()

def copy():
    keyboard.press(Key.ctrl)
    tap('c')
    keyboard.release(Key.ctrl)

def parseInfo():
    """
    Extract Name and Quantity from our clipboard
    """
    if(cb.paste() != 'DEFAULT'):#Our clipboard will be reset after each item check. This checks to make sure a clean clipboard is coming in
        text = cb.paste()
        filteredText = text.splitlines()
        itemName = filteredText[1]
        separator = '/'
        itemQuant = filteredText[3]
        itemQuantFiltered = itemQuant.replace('Stack Size: ', '')
        itemQuantFiltered = itemQuantFiltered.split(separator,1)[0]
        itemQuant = itemQuantFiltered
        cb.copy('DEFAULT')#Sets the clipboard so items arent scanned twice. (repeat clipboard usage)
        return (itemName, int(itemQuant))
    return ('None',-1)


time.sleep(2.0)
#checkSlot(0,0)
getTradeContents('Scroll of Wisdom',38)#We need to parse incoming trade, and supply this function with the type and quant--
#--->that we are expecting.





"""
To check if we are in a trade, send trade request with /tradewith @playername
then whipser ourselves a string and detect if that string is found before 'Trade Cancelled'
is found. Only check every 1.25-2seconds to limit cpu usage.
"""
