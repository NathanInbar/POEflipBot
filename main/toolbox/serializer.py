#from toolbox.general import *
from general import *
import os, re

localpath = getProjectPath()+'\\serialized.txt'#"main\\toolbox\\serialized.txt"
#"C:\\Users\\robot\\OneDrive\\Documents\\Python Projects\\POEflipBot\\main\\toolbox\\testDoc.txt"
def readSerialized():
    """ reads the serialized.txt and prints its content """
    with open(localpath, 'r') as f:
        f_contents = f.read()
        print(f_contents)

def writeSerialized(text, txtVariable):
    """ text is what variable you want to serialize, varibale is custom so maybe is the @dir: or maybe its the @example:
        this func will:
        1)save a copy of the pre-edited txt into 'data'
        2)take the input, see if there is already the txtVariable saved, and append it if it isnt
    """

    with open(localpath, 'r+') as f:
        data = f.read()

    with open(localpath, 'a') as f:
        if txtVariable not in data:
            f_contents = f.write(text)

def getTextVariable(txtVariable):
    """ returns the value for the text variable that has been serialized """
    with open(localpath, 'r') as f:
        data = f.read()
        for item in data.split("\n"):
            if txtVariable in item:
                return (re.sub('{}:'.format(txtVariable),'',item.strip()))

def isVariableExists(txtVariable):
    """ returns boolean whether the variable is saved or not """
    with open(localpath, 'r') as f:
        data = f.read()
        for item in data.split("\n"):
            if txtVariable in item:
                return True


#print(localpath)
#print(getTextVariable('@dir'))
#print(isVariableExists('@dir'))
