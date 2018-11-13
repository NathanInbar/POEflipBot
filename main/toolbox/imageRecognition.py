
"""
PoeFlipBot utilizes image recognition to verify the amount and type of each currency entering and exiting
each trade. This is crucial for the integrity and efficiency of the bot itself.
"""

import time, sys, random
import numpy as np
#from skimage.measure import structural_similarity as ssim
import cv2
import pyautogui
import imutils
from inventory import *#toolbox.
from general import *#toolbox.
import glob

cols = 12
rows = 5

currency_images = []
quant_images = []
iconFolder = getResourcePath() + '\\PoE-Currency-Icons\\'
quantFolder = getResourcePath() + '\\Quantity\\'

"""-1 means we arent 100% sure what it is"""

#currency_images.append(cv2.imread(iconFolder +"blank.png"))
#currency_images.append(cv2.imread(iconFolder +"1.png"))#alt(1)
#currency_images.append(cv2.imread(iconFolder +"2.png"))#fusing(2)
#currency_images.append(cv2.imread(iconFolder +"3.png"))#alchemy(3)
#currency_images.append(cv2.imread(iconFolder +"4.png"))#chaos (4)

#img_a = cv2.imread("main\\resources\\PoE-Currency-Icons\\test_compressed.png")
#img_b = cv2.imread("main\\resources\\PoE-Currency-Icons\\test_cropped.png")


currently_in_offer_window = []
offer = []
"""
Basically, read part of screen (i.e: inventory, trade window, stash) and parse its currency type and quantity (white text top left))
Compare screencap to database of locally saved currency images. (loop through all, and take highest probability one)
"""
#Currency Icons (59x59) are stored in main/resources/PoE-Currency-Icons  each image corresponds to its Item ID according to readME
def mse(img_a,img_b):#Returns the mean squared error (popular image comparision must be same dimensions)
    err = np.sum( (img_a.astype("float") - img_b.astype("float")) ** 2 )
    err /= float(img_a.shape[0] * img_b.shape[1])
    print(err)
    return err
def checkSlot(x,y):#checks invetory slot
    quantity = 1
    slot_cords = moveToSlot(x,y,True)#use the coordinates of each slot of imageRecognition
    img_grab = pyautogui.screenshot(region = (slot_cords[0],slot_cords[1],26,26 ))#was 29,29

    img_grab = cv2.cvtColor(np.array(img_grab), cv2.COLOR_RGB2BGR)
    quant_img_ones = img_grab[0:9, 5:11]#6x9
    quant_img_tens = img_grab[0:9, 0:6]#6x9
    #cv2.imwrite("C:\\Users\\Cptcr\\OneDrive\\Documents\\GitHub\\POEflipBot\\main\\resources\\Quantity\\new.png",quant_img_ones)
    #print(findQuantMatch(quant_img_tens))
    if (findQuantMatch(quant_img_ones) == -1 ):#if the ones place doesnt find a match we know the value is less than 10
        quantity = findQuantMatch(quant_img_tens)
        print('No Tens Place')#i.e less than 10
    else:
        quantity = int(  str(findQuantMatch(quant_img_tens)) + str(findQuantMatch(quant_img_ones)) )

    print(quantity)
    #cv2.imshow("img", quant_img_ones) # to view the image (debug)
    #cv2.waitKey(0)# to view the image (debug)

    #Do the logic here to detect what id and quant the item is.

    #id = findMatch(img_grab) # TO-DO: LOGIC (with image recog)

    #print(id)
    # TO-DO: LOGIC (with image recog)
    slot_offer = (id,quantity) # nicely packed tuple to pass as an arg
    #if the slot is blank we shouldn't append anything.
    currently_in_offer_window.append(  slot_offer  )# what the checked slot is offering and append it.

def findMatch(img_grab):
    lowest = 1000000
    index = -1
    """Compare grabbed slot to all currency images"""
    for x in range(len(currency_images)):
        diff = mse(img_grab,currency_images[x])
        if (diff < lowest):
            lowest = diff
            index = x
    if (lowest < 12500):#within reasonable matching
        return index + 1 # ID
    else:#not a match
        return -1

def findQuantMatch(img_grab):
    lowest = 1000000
    index = -1
    """Compare grabbed slot to all Quantity images"""
    for x in range(len(quant_images)):
        diff = mse(img_grab,quant_images[x])
        if (diff < lowest):
            lowest = diff
            index = x
    if (lowest < 12500):#within reasonable matching
        return index  # ID
    else:#not a match
        return -1

def checkTradeWindow():#12x5 (12 columns, 5 rows)
    """Will check every slot in the trade window and log its type and amount"""
    for y in range(cols):
        for x in range(rows):
            checkSlot(y,x)#for every slot, read the ID and quant
    sortOffered()

def sortOffered(offered = currently_in_offer_window,sort = [],first = True):
    global offer
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

def getOffer():
    return offer

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

def addImagesToList():
    for x in range (1,25):#how many images are in the PoeCurrencyIcons Folder
        currency_images.append(cv2.imread(iconFolder + str(x) +".png"))
    currency_images.append(cv2.imread(iconFolder +"45.png"))
    currency_images.append(cv2.imread(iconFolder +"46.png"))
    currency_images.append(cv2.imread(iconFolder +"47.png"))
    currency_images.append(cv2.imread(iconFolder +"69.png"))
    currency_images.append(cv2.imread(iconFolder +"blank.png"))
    for x in range(10):
        quant_images.append(cv2.imread(quantFolder + str(x)+".png"))



addImagesToList()#adds all images from the PoeCurrencyIcons folder to a list
#^ Ask nathan how to only have to do this once
time.sleep(2)
#checkTradeWindow()
#sortOffered(currently_in_offer_window,[])
checkSlot(0,0)




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
