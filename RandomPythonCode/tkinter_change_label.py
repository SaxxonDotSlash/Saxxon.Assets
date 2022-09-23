from tkinter import *


def chlbl():
    label.config(text='Change the value')

root = Tk()

label = Label(root, text='Hello').pack()
change = Button(root, text='change', command=chlbl).pack()

root.mainloop()