from tkinter import *
import sys

window = Tk()
window.title("Welcome")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=2, row=0)
btn = Button(window, text="Quit", command=sys.exit)
btn.grid(column=1, row=0)
window.mainloop()