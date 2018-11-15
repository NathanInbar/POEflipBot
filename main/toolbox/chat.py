#from toolbox.general import *
#from toolbox.serializer import *
from general import *
from serializer import *
#C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs\Client.txt

clientLogPath = "{}\\logs\\Client.txt".format(getTextVariable('@dir'))

def clearTextBox():
    tap(Key.enter)
    keyboard.press(Key.ctrl)
    tap('a')
    keyboard.release(Key.ctrl)
    tap(Key.backspace)
    tap(Key.esc)

def typeMessage(message, channel):# message to be sent, || channel d @character = whisper, % = party, etc. (LOCAL [blank] DOES NOT WORK)
    tap(Key.enter)
    keyboard.type(channel + ' ' + message)
    tap(Key.enter)

def readLogLast():
        """ reads client.txt and prints the last line of it's content """
        with open(clientLogPath,encoding="utf8") as f:
            f_contents = f.readlines()
            return f_contents[-1]

def readMessage():
    """ cleans up the chat logs to only display the name of the person sending it, and the message sent """
    lastLog = readLogLast()
    if '@From' in lastLog:
        trimmed = lastLog[59:]#if its from someone the username will start on the 59th character
        return trimmed.split(': ')

def isMessageTrade(message):
    """ the argument should be readMessage[1] """
    if "Hi, I'd like to buy your" in message:
        return True

def dissectTrade(message):
    """returns a list with 4 elements: {how much, of what they want to buy, for how much, of what we are selling}"""
    newMsg = {message.replace("Hi, I'd like to buy your ",'').replace("for my ",'').replace(" in {}.".format(league),'')}
    return str(newMsg).split()
# - - - -
def chatReadLoop():
    """ loop method to be run on thread by main.py """
    while True:
        time.sleep(1)
        print(readMessage())
