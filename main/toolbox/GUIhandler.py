from serializer import *
from tkinter import *
import time

#C:\Program Files (x86)\Grinding Gear Games\Path of Exile


def promptForDirectory():
    """ prompts user for the path to poe """
    root = Tk()

    root.geometry("500x110")

    def retrievePathInput():
        inputValue = textBox.get("1.0","end-1c")
        writeSerialized("@dir:{}\n".format(inputValue), '@dir:')
        root.quit()

    label = Label(root, text="path to POE main dir (EXAMPLE C:\Program Files (x86)\Grinding Gear Games\Path of Exile)")
    label.pack()

    textBox = Text(root, height=1, width=50)
    textBox.pack()

    buttonCommit = Button(root,height=1,width=10,text="Done",command=lambda: retrievePathInput())
    buttonCommit.pack()
    mainloop()

def checkVariableDefs():
    if(isVariableExists('@dir')==None):
        """if the user has not previously entered their POE directory, prompt them to do so"""
        promptForDirectory()
