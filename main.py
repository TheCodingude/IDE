from tkinter import *



HEIGHT = 400
WIDTH = 50


window = Tk()

textbox = Text(window, fg="white", bg="#2e2e2d", width=WIDTH, insertbackground="white")
textbox.pack(fill="both", expand=True)



commandbox = Text(window, bg="#2e2e2d", fg="white", width=WIDTH, height=1, insertbackground="white")
commandbox.pack(fill="both", expand=True)





window.mainloop()