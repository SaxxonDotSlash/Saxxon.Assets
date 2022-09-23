from tkinter import *
import random as r


#def randnum():
#    x = r.randint(0,9)
#    print(x)

##Variables
ID1 = 0
ID2 = 0
ln = 'placeholder'
fn= 'placeholder'

##Lists
fname = ['James', 'John', 'Guy']

lname = ['Schreiner', 'Doe', 'Dude']

##Functions
def ClickExitButton():
    exit()

def Random_ID():
    fnl = len(fname)
    lnl = len(lname)
    r1 = r.randint(0, fnl)
    r2 = r.randint(0, lnl)
    ID1 = str(r1)
    ID2 = str(r2)
    print("ID1 is " + ID1)
    print("ID2 is " + ID2)

def display_name():
    display = Tk()

    first = Label(display, text=ln).grid(row=1, column=1)
    last = Label(display, text=fn).grid(row=2, column=1)
    exit = Button(display, text='Exit', command=ClickExitButton).grid(row=3, column=1)

    display.mainloop()

def gen_name():
    Random_ID()
    fni = fname[2]
    lni = lname[2]
    fn = str(fni)
    ln = str(lni)
    print("First name is " + fn)
    print("Last name is " + ln)
    display_name()

#GUI Window
root = Tk()

#randnum = Button(root, text="random", command=randnum).grid(row=1, column=3)

generate_name_button = Button(root, text='Generate Name!', command=gen_name).grid(row=1, column=1)

exit_button = Button(root, text='Exit', command=ClickExitButton).grid(row=5, column=1)

root.wm_geometry('200x50')
root.wm_title('Name Generator')
root.mainloop()