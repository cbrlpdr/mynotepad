import tkinter
import os
from tkinter import*
from tkinter.messagebox import*
from tkinter.filedialog import*

class Notepad:
    __root = Tk()
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    #Scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)

    __file = None