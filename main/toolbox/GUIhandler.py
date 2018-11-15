#from toolbox.serializer import *
#from toolbox.general import *
from general import *
from serializer import *
from tkinter import *
import tkinter as tk
from tkinter import ttk
#
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
#
import time

#C:\Program Files (x86)\Grinding Gear Games\Path of Exile
icoPath = getResourcePath() + '\\other\\poeflipicon.ico'

def mainGUI():
    root = Tk()
    root.geometry("600x500")
    root.winfo_toplevel().title("POE Flip Bot v{0}".format(version))
    root.resizable(False, False)
    root.iconbitmap(icoPath)

    rows=0
    while rows<50:
        root.rowconfigure(rows,weight=1)
        root.columnconfigure(rows,weight=1)
        rows+=1

    nb = ttk.Notebook(root)
    nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

    page1 = ttk.Frame(nb)
    page2 = ttk.Frame(nb)
    page3 = ttk.Frame(nb)
    nb.add(page1, text='Menu')
    nb.add(page2, text='CPU Monitor')
    nb.add(page3, text='Log')

    #widgets
    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    a.plot([1,2,3,4,5,6,7,8],[5,6,2,6,2,6,6,2])

    canvas = FigureCanvasTkAgg(f, page2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,expand=True)

    mainloop()

# - - - - -

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

#checkVariableDefs()
mainGUI()
