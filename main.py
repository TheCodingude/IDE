from tkinter import *
from tkinter.ttk import Notebook
from tkinter import filedialog

import os

files = {}

def add_tab(contents, name, filepath):
    text = Text(undo=True)
    files[filepath] = text
    
    tabs.add(text, text=name)
    text.insert('end', contents)

def openFile(*args):

    files = filedialog.askopenfilenames()

    if not files:
        return
    
    for file in files:

        with open(file, "r") as f:

            text = f.read()

            add_tab(text, os.path.basename(file), file)


n = 0

window = Tk()
window.geometry("400x400")

# Key Bindings

window.bind("<Control-o>", openFile)




tabs = Notebook(window)
tabs.pack(expand=True, fill="both")



window.mainloop()