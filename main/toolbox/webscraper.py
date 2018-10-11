from lxml import html
from math import floor
import requests, re, string

#"http://currency.poe.trade/search?league=Delve&online=x&stock=&want={}&have={}".format(id1,id2)
#XPATH //*[@id=\"content\"]/div[@class=\"displayoffer \"]/div[@class=\"row\"]/div[@class=\"large-6 columns\"]/div/div/div[2]/div[3]/text()

def getPrices(id1, id2, size=5, side=0):#id1/id2 range from poe website, size is how many items down the list you want, side is which side of the margin you want range 0 or 1, rounded = should list be rounded to hundredths
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
            textAsNum = float(text)
            prices.append(round(float(text),2))
    return prices

def getPricesWithReciprocal(id1, id2, size=5, side=0):
    prices = [getPrices(id1,id2,size,side), getPrices(id2,id1,size,abs(side-1))]
    return prices

def getBestMargin(prices):
    return round((float(prices[0][0]) - float(prices[1][0])), 2)

print(getPrices(4,9,5))
#print(getPricesWithReciprocal(4,9))
#prices = getPricesWithReciprocal(4,9)
#print('{} | {} | {}'.format(prices[0][0],prices[1][0],getBestMargin(prices)))
