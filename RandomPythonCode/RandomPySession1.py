#Random Session 1
#SongSticker

##TODO##
#brainstorm catchy song phrases
#assign numbers to phrases
#program random number generator to select phrase
#display catchy phrase

from tkinter import * 
import random

def randnum():
    x = random.randint(0, 9)
    y = x

    print("Random phrase is: " + y)
    

PhraseList = ["Catchy", "Song", "Phrases", "Go", "Here."]
#Test to print list#print(PhraseList)#Debug
root = Tk()

RandomPhraseButton = Button(root, text="Catchy Phrase").pack()

root.wm_title("SongSticker v1")
#root.geometry(500x500)
root.mainloop()