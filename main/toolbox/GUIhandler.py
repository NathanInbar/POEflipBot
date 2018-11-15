#from toolbox.serializer import *
#from toolbox.general import *
from general import *
from chat import *
from serializer import *
#
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
#style.use("ggplot")#dark_background, ggplot, grayscale
style.use("dark_background")
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

xList = []
yList = []


def animate(i):

    cpu = int(psutil.cpu_percent(interval=.5,percpu=False))


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
    nb.add(page2, text='   Log   ')
    nb.add(page3, text='CPU Monitor')
#Menu --------------------------------------------------------------------------
    settingsLabel = Label(page1,text='Correct POE Settings: ', font = ('Comic Sans MS', 24))
    settingsLabel.pack()
    check1 = Checkbutton(page1,text='800x600 window', font = ('Helvetica', 16))
    check1.pack()
    check2 = Checkbutton(page1,text='Lock cursor to window', font = ('Helvetica', 16))
    check2.pack()

#end Menu ----------------------------------------------------------------------
#Log ---------------------------------------------------------------------------
    S = Scrollbar(page2)
    T = Text(page2, height=4, width=75)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END, readLog())
    T.config(state=DISABLED)

    def updateLog():
        #print('PASS: updateLog')
        with open(logPath,"r") as f:
            data = f.read()
            T.config(state=NORMAL)
            ScrollbarPos = S.get()
            T.delete("1.0", "end")
            T.insert(END,data)
            T.yview_moveto(ScrollbarPos[0])
            T.config(state=DISABLED)
        T.after(1000, updateLog)

    T.after(1000, updateLog)
#end Log -----------------------------------------------------------------------
#cpu monitor--------------------------------------------------------------------
    canvas = FigureCanvasTkAgg(f, page3)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,expand=True)
    canvas.draw()

    ani = animation.FuncAnimation(f, animate, interval=500)
#end cpu monitor----------------------------------------------------------------
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
