from tkinter import *

#Initialize
main = Tk()

#Top Tabs
home = Button(main, text="Home", padx=3, pady=3).grid(column=0, row=0)
settings = Button(main, text="Settings", padx=3, pady=3).grid(column=1, row=0)
contact = Button(main, text="Contact Us", padx=3, pady=3).grid(column=2, row=0)
apps = Button(main, text="Apps", padx=3, pady=3).grid(column=0, row=1)


#Window Stuff
#main.geometry("500x500")
main.title("Welcome to the Idle.co Menu")
main.mainloop()