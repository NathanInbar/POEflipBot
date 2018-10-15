from lxml import html
from math import floor,ceil
import requests, re, string
from statistics import mean, median
from pandas import *
import numpy as np

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
    17 : 'wisdom scrolls',
    18 : 'portal scrolls',
    19 : 'armour',
    20 : 'whetstone',
    21 : 'glassblowers',
    22 : 'transmutes',
    23 : 'augmentation',
    24 : 'mirror',
}

illegalIDs = [0,17,18,19,20]#these are low level items that we want to skip like wisdom scrolls

#"http://currency.poe.trade/search?league=Delve&online=x&stock=&want={}&have={}".format(id1,id2)
#XPATH //*[@id=\"content\"]/div[@class=\"displayoffer \"]/div[@class=\"row\"]/div[@class=\"large-6 columns\"]/div/div/div[2]/div[3]/text()

def getPrices(id1, id2, size=5, side=0):#id1/id2 range from poe website, size is how many items down the list you want, side is which side of the margin you want range 0 or 1, rounded = should list be rounded to hundredths
    url = "http://currency.poe.trade/search?league=Delve&online=x&stock=&want={}&have={}".format(id1,id2)
    response = requests.get(url)
    source = response.content
    htmlElem = html.document_fromstring(source)
    smallElems = htmlElem.cssselect("small")

    x=0
    prices = []
    for elem in smallElems:

        text = elem.text_content()
        text = re.sub("[^0123456789\.]","",text)
        text = text[1:]
        if(x % 2 == side and x < (size*2) and text is not ''):#side = 0 means left, side = 1 means right of margin numbers
        #size multiplied by 2 to account for both sides of the numbers
            #print('\'{}\''.format(text))
            textAsNum = float(text)
            prices.append(textAsNum)
            #prices.append(round(float(text),2))
        x+=1
    return prices
    #return prices

def getPricesWithReciprocal(id1, id2, size=10, side=0):
    prices = [getPrices(id1,id2,size,side), getPrices(id2,id1,size,abs(side-1))]
    return prices

def filterOutliersFromList(inpList):
    #""" argument list must be size 10 (or change the static q1 and q3 indexes to dynamically calculate it) """
    newList = []
    listMedian = median(inpList)#median is q2

    q1 = inpList[0:len(inpList)//2]
    q3 = inpList[len(inpList)//2:len(inpList)]

    q1 = median(q1)
    q3 = median(q3)

    #q3 = median(q3)
    IQR = q3-q1
    outerFence = round((IQR * 1.5)+q3,2)
    innerFence = round((IQR * -1.5)+q1,2)

    i = 0
    for num in inpList:
        if num < outerFence and num > innerFence:
           newList.append(num)
    #print("median:{}, q1:{}, q3:{}, IQR:{}, outerFence:{}, innerFence:{}".format(listMedian,q1,q3,IQR,outerFence,innerFence))
    return newList


def filterOutliersFromLists(list2d):
    newList2d=[[]]
    #newList2d.append(filterOutliersFromList(list2d[0]))
    #newList2d.append(filterOutliersFromList(list2d[1]))
    return list2d

def trimLists(list2d):#GET BEST MARGIN DEPRECATED; USE RETURN FROM TRIMLISTS
    """return the first value of each list as a tuple"""
    newList=[]
    newList = [x for x in list2d if x != []]
    ntl = (list2d[0][0],list2d[1][0])
    return ntl
    #return newList

def calcMargin(bestPricesAsTuple):
    return abs(bestPricesAsTuple[0] - bestPricesAsTuple[1])

def getFMR(id1,id2):#full list treatment & margin return, ready to be packed into a cell
    """This will return the margin in currency of ID 2 (ex: 1,2 returns a profit margin of 0.1 of id2 per trade)
    - these margin values will be stored in the .csv, and when they are read they will be converted to chaos,
    converted it inside getFMR is a LOT more inefficient although possible
    """
    priceList2d = getPricesWithReciprocal(id1,id2,5)#size is arbitrary
                #current problem: substituting 1 and 2 with id1 and id2 gives an index out of bounds exception
    if priceList2d[0] and priceList2d[1]:
        filtered2dlist = filterOutliersFromLists(priceList2d)
        trimmedLists = trimLists(filtered2dlist)
        margins = calcMargin(trimmedLists)
    else: margins = 0
    #return round(margins,2)
    return margins
# - - -

def fullMarketLoop(x=24):
    """ (args) = the current amount of item ids

    THE MARGIN THAT IS PUT INTO THE TABLE IS HOW MUCH OF CURRENCY ID2 YOU WILL PROFIT
    """
    x+=1
    y = x
    table = {}
    for i in range(x):
        for j in range(y):#edit the range for debugging purposes
            if i != j and (illegalIDs.count(i)==0) and (illegalIDs.count(j)==0): #is not in the list of illegal characters
                print(i,j)
                table[i,j] = getFMR(i,j)
                if table[i,j] == None:
                    table[i,j] = 0
                print(table[i,j])
    df = DataFrame.from_dict(table,orient="index")
    df.to_csv('table.csv')

#print(fullMarketLoop(24))
#14 minutes and 15 seconds
#print(calcMargin(trimLists(filterOutliersFromLists(getPricesWithReciprocal(6,24)))))
#fullMarketLoop(24)#argument = amount of items to go down the list
#print(fullMarketLoop(24))
#11.8min
print(getFMR(6,24))
