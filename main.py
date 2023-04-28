import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    __root = Tk()
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar)
    __thisEditMenu = Menu(__thisMenuBar)
    __thisHelpMenu = Menu(__thisMenuBar)

    # Scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)

    __file = None

    def __init__(self, **kwargs):
        # Set icon
        try:
            self.__root.wm_iconbitmap("./favicon.ico")
        except:
            pass

        # Set window size
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set title
        self.__root.title("New file - MyNotepad")

        # Center the window text
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # Alignments
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' %
                             (self.__thisWidth, self.__thisHeight, left, top))

        # Making the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(8, weight=1)

        # Add controls
        self.__thisTextArea.grid(sticky=N + E + S + W)

        # Adding commands: New, Open and Save
        self.__thisFileMenu.add_command(label="New", command=lambda self=self: self.__new_file())
        self.__thisFileMenu.add_command(label="Open", command=lambda self=self: self.__open_file())
        #self.__thisFileMenu.add_command(label="Save", command=self.__save_file())

        self.__thisFileMenu.add_separator()
        #self.__thisFileMenu.add_command(label="Exit", command=self.__quit_app())

        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        self.__root.config(menu=self.__thisMenuBar)
        #self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        # Scrollbar content auto-adjust
        #self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        #self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quit_app(self):
        self.__root.destroy()

    def __open_file(self):
        self.__file = askopenfilename (defaultextension=".txt",
                                      filetypes=[("All Files", '*.*'), ("Text Documents", "*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - MyNotepad")
            self.__thisTextArea.delete(1.0, END)
            file = open(self.__file, "r")
            self.__thisTextArea.insert(1.0, file.read())
            file.close()

    def __new_file(self):
        self.__root.title("Untitled - MyNotepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __save_file(self):
        if self.__file is None:
            self.__file = asksaveasfilename(initalfile='Untitled.txt', defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file, 'w')
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + " - MyNotepad")
        else:
            file = open(self.__file, 'w')
            file.write(self.__thisTextArea.get(1.8, END))
            file.close()



    def run(self):
        self.__root.mainloop()


notepad = Notepad(width=600, height=800)
notepad.run()
