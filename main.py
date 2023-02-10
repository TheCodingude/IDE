from tkinter import *


def end_paren(*args):

    insert = textbox.index(INSERT)
    textbox.insert(insert, ")")


def end_curly(*args):

    insert = textbox.index(INSERT)
    textbox.insert(insert, "}")



HEIGHT = 400
WIDTH = 50


window = Tk()

window.bind("<(>", end_paren)
window.bind("<{>", end_curly)

textbox = Text(window, fg="white", bg="#2e2e2d", width=WIDTH, insertbackground="white", tabs=16)
textbox.pack(fill="both", expand=True)


commandbox = Text(window, bg="#2e2e2d", fg="white", width=WIDTH, height=1, insertbackground="white")
commandbox.pack(fill="both", expand=True)





window.mainloop()