#attempt 3
import Tkinter
#import _tkinter
from Tkinter import *
#from _tkinter import *

HEIGHT = 700
WIDTH = 800

root = tkinter.Tk()

canvas = tkinter.Canvas(root, height = HEIGHT, width=WIDTH)
canvas.pack()

frame = tkinter.Frame(root, bg='red')
frame.pack()

testlabel = Label(root, text="Hello World!").pack()


root.mainloop()
