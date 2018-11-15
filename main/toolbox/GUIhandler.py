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
import matplotlib.animation as animation
from matplotlib import style
#
import psutil
import time

#C:\Program Files (x86)\Grinding Gear Games\Path of Exile
icoPath = getResourcePath() + '\\other\\poeflipicon.ico'

style.use("ggplot")#dark_background, ggplot, grayscale

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

xList = []
yList = []
def animate(i):

    cpu = int(psutil.cpu_percent(interval=.4,percpu=False))

    xList.append(i)
    yList.append(cpu)

    a.clear()
    a.plot(xList, yList)

    if len(xList) > 30:
        del xList[0]
        del yList[0]

    a.set_title('CPU Usage Over Time')
    a.set_xlabel('Elapsed Time (seconds)')
    a.set_ylabel('CPU Usage (percent)')

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
    canvas = FigureCanvasTkAgg(f, page2)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,expand=True)
    canvas.draw()

    ani = animation.FuncAnimation(f, animate, interval=500)
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
