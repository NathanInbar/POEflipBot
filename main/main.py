from toolbox.general import *
from toolbox.chat import *
from toolbox.inventory import *
from toolbox.webscraper import *
from toolbox.imageRecognition import *
from toolbox.marketManager import *
from toolbox.GUIhandler import *
import threading as mp
import sys
#required python modules:
#pynput, (lxml, requests, cssselect,)<-webscrape
#(numpy,opencv-python, scikit-image, imutils, pyobjc-core, pyautogui)<-- image recognition
#(pandas)<-dataframes/writing to csv

#def marketReadLoop():
if __name__ == "__main__":
    pass
    #SERIALIZING
    checkVariableDefs()
    #--end serializing

    #MULTITHREADING
    #chatRead = mp.Thread(target=chatReadLoop)
    #test = mp.Thread(target=testProcess)
    ##chatRead.start()
    #test.start()
    ##chatRead.join()
    #test.join()
    #--end multithreading

    #TRADE OFFER IMAGE RECOGNITION
    #time.sleep(5)
    #checkTradeWindow()
    #print(getOffer())
    #--end trade offer recognition
