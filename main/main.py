from toolbox.general import *
from toolbox.chat import *
from toolbox.inventory import *
from toolbox.webscraper import *
from toolbox.imageRecognition import *
from toolbox.marketManager import *
from toolbox.GUIhandler import *
import threading as mp
#from toolbox.marketManager import *
#required python modules: pynput, (lxml, requests, cssselect,)<-webscrape, pandas
#uninstall (no longer needed): (oauth2client, PyOpenSSL, gspread)<-google spreadsheets
#(numpy,opencv-python, scikit-image, imutils, pyobjc-core, pyautogui)<-- image recognition
#print(dissectTrade(readMessage()[1]))
"""
def testProcess():
    i = 1
    while( i < 5):
        time.sleep(1)
        print(i)
        i+=1
"""
def chatReadLoop():
    while True:
        time.sleep(1)
        print(readMessage())

#def marketReadLoop():
if __name__ == "__main__":
    chatRead = mp.Thread(target=chatReadLoop)
    #test = mp.Thread(target=testProcess)
    chatRead.start()
    #test.start()
    ##chatRead.join()
    #test.join()
    #--end multithreading

    #TRADE OFFER IMAGE RECOGNITION
    #time.sleep(5)
    #checkTradeWindow()
    #print(getOffer())
    #--end trade offer recognition
