from lxml import html
from math import floor
import requests, re, string
from statistics import mean, median
from pandas import *

#"http://currency.poe.trade/search?league=Delve&online=x&stock=&want={}&have={}".format(id1,id2)
#XPATH //*[@id=\"content\"]/div[@class=\"displayoffer \"]/div[@class=\"row\"]/div[@class=\"large-6 columns\"]/div/div/div[2]/div[3]/text()

def getPrices(id1, id2, size=10, side=0):#id1/id2 range from poe website, size is how many items down the list you want, side is which side of the margin you want range 0 or 1, rounded = should list be rounded to hundredths
    url = "http://currency.poe.trade/search?league=Delve&online=x&stock=&want={}&have={}".format(id1,id2)
    response = requests.get(url)
    source = response.content
    htmlElem = html.document_fromstring(source)
    smallElems = htmlElem.cssselect("small")

    x=-1
    prices = []
    for elem in smallElems:
        x+=1
        text = elem.text_content()
        text = re.sub("[^0123456789\.]","",text)
        text = text[1:]
        text = text
        if(x % 2 == side and x < (size*2)):#side = 0 means left, side = 1 means right of margin numbers
            print(text)
            textAsNum = float(text)
            prices.append(round(float(text),2))
    return prices

def getPricesWithReciprocal(id1, id2, size=10, side=0):
    prices = [getPrices(id1,id2,size,side), getPrices(id2,id1,size,abs(side-1))]
    return prices

def convertToChaos(id):
    return mean(getPrices(id,4,5,0))

def filterOutliersFromList(list):
    """ argument list must be size 10 (or change the static q1 and q3 indexes to dynamically calculate it) """
    newList = []
    listMedian = median(list)
    q1 = list[2]
    q3 = list[7]
    IQR = q3-q1
    outerFence = (IQR * 1.5)+q3
    innerFence = (IQR * -1.5)+q1

    i = 0
    for num in list:
        if num < outerFence or num < innerFence:
            newList.append(num)
    return newList #"median:{}, q1:{}, q3:{}, IQR:{}, outerFence:{}, innerFence:{}".format(listMedian,q1,q3,IQR,outerFence,innerFence)

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
    return round(calcMargin(trimLists(filterOutliersFromLists(getPricesWithReciprocal(id1,id2)))),2)
# - - -
def fillHeaders():
    headers = []
    for i in range(0,24):
        headers.append(i)
    return headers

def fullMarketLoop():
    table1 =[[0.0,0.1,0.2,0.3],
            [1.0,1.1,1.2,1.3],
            [2.0,2.1,2.2,2.3],
            [3.0,3.1,3.2,3.3]]
    #table = [column][row]
    #print(table1[1][0])=1.0
    headers = fillHeaders()
    table = []
    for i in range(1,24):
        new = []
        for j in range(1,24):
            new.append(getFMR(i,j))
        table.append(new)



    df = DataFrame(table, columns=headers)
    df.to_csv('table.csv',index=False)

    #FILL headers


#test = [1,2,3,4,5,6,7,8,9,100]
#print(filterOutliers(test))

#print(getPricesWithReciprocal(1,4,side=1))
#print(getBestMargin(getPricesWithReciprocal(1,4,side=1)))

#print(getBestMargin(getPricesWithReciprocal(1,4,5)))
#print(getPricesWithReciprocal(4,9))
#prices = getPricesWithReciprocal(4,9)
#print('{} | {} | {}'.format(prices[0][0],prices[1][0],getBestMargin(prices)))
#print (convertToChaos(6))

#fullMarketLoop()
getFMR(1,1)
