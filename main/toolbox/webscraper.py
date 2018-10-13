from lxml import html
from math import floor,ceil
import requests, re, string
from statistics import mean, median
from pandas import *
import numpy as np

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
        if(x % 2 == side and x < (size*2)):#side = 0 means left, side = 1 means right of margin numbers
        #size multiplied by 2 to account for both sides of the numbers
            textAsNum = float(text)
            prices.append(textAsNum)
            #prices.append(round(float(text),2))
        x+=1
    return prices
    #return prices

def getPricesWithReciprocal(id1, id2, size=10, side=0):
    """MUST RETURN A LIST WITh EVEN NUMBER OF ITEMS """
    prices = [getPrices(id1,id2,size,side), getPrices(id2,id1,size,abs(side-1))]
    return prices

def convertToChaos(id):
    return mean(getPrices(id,4,5,0))

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
    newList2d = [[]]
    for list in list2d:
        newList2d.append(filterOutliersFromList(list))
    return newList2d

def calcMargin(bestPricesAsTuple):
    return bestPricesAsTuple[0] - bestPricesAsTuple[1]

def trimLists(list2d):#GET BEST MARGIN DEPRECATED; USE RETURN FROM TRIMLISTS
    newList=[]
    for ls in list2d:
        newList.append(ls[:1])
    newList = [x for x in newList if x != []]
    ntl = (newList[0][0],newList[1][0])
    return ntl

def getFMR(id1,id2):#full list treatment & margin return, ready to be packed into a cell
    priceList2d = getPricesWithReciprocal(1,2,5)
    filtered2dlist = filterOutliersFromLists(priceList2d)
    trimmedLists = trimLists(filtered2dlist)
    margins = calcMargin(trimmedLists())
    return round(margins)#round(calcMargin(trimLists(filterOutliersFromLists(getPricesWithReciprocal(id1,id2)))),2)
# - - -

def fullMarketLoop():
    table = {}
    for i in range(24):
        for j in range(24):
            table[i,j] = getFMR(i,j)

    df = DataFrame.from_dict(table,orient="index")
    df.to_csv('table.csv')

#print(getFMR(1,2))

getFMR(1,2)
