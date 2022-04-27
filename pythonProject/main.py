import numpy as np
import random


class Shoe:
    def __init__(S):
        S.Cards = []
        deck = []
        for x in range(1, 14):
            for y in range(0, 8):
                deck.append(x)
        S.Cards = deck


class Hand:
    def __init__(H):
        H.hand = []


class Round:
    def __init__(R):
        R.S = Shoe()
        R.Player = Hand()
        R.Dealer = Hand()
        R.count = 0

    def shuffle(R):
        random.shuffle(R.S.Cards)
        random.shuffle(R.S.Cards)
        random.shuffle(R.S.Cards)

    def newRound(R):
        R.Player.hand.clear()
        R.Dealer.hand.clear()
        R.hit("P")
        R.hit("P")
        R.hit("D")
        R.hit("D")

    def hit(R, user):
        if user == "P":
            card = R.S.Cards[0]
            if card >= 10:
                R.count -= 1
            elif card < 7:
                R.count += 1
            R.S.Cards.pop(0)
            R.Player.hand.append(card)
        elif user == "D":
            card = R.S.Cards[0]
            if card >= 10:
                R.count -= 1
            elif card < 7:
                R.count += 1
            R.S.Cards.pop(0)
            R.Dealer.hand.append(card)


R1 = Round()
R1.shuffle()
R1.newRound()
R1.Player.hand


from tkinter import *
from tkinter import ttk
from tkmacosx import Button
from tkmacosx import CircleButton # used to change button colour
from PIL import ImageTk, Image

# Import tkinter library

# Create an instance of Tkinter frame or window
win = Tk()
stscreen = Tk();

# Set the geometry of tkinter frame
stscreen.geometry("450x450")
win.geometry("1200x900")
win.config(background='#35654d')
stscreen.config(background='#35654d')
win.withdraw()
stscreen.eval('tk::PlaceWindow . center')
# establish commands
def startgame():
    if diffic != None:
        stscreen.destroy()
        win.deiconify()
    else:
        sel.grid()

    #if diffuclty hasnt been pressed, dont start game



def establishround():
    global R1
    start.config(text="Stop")
    R1 = Round()
    R1.shuffle()
    R1.newRound()
    # need code to establish round


def quit():
    #win.iconify()
    win.destroy()


def deal():
    hander = R1.Player.hand
    global card_1
    global card_2
    filestring1 = "/Users/emersondetering/Downloads/BlackJackPython/png/" + str(hander[0]) + "_of_clubs.png"
    filestring2 = "/Users/emersondetering/Downloads/BlackJackPython/png/" + str(hander[1]) + "_of_clubs.png"
    if hander[0] == 11:
        filestring1 = "/Users/emersondetering/Downloads/BlackJackPython/png/jack_of_clubs.png"
    if hander[0] == 12:
        filestring1 = "/Users/emersondetering/Downloads/BlackJackPython/png/queen_of_clubs.png"
    if hander[0] == 13:
        filestring1 = "/Users/emersondetering/Downloads/BlackJackPython/png/king_of_clubs.png"
    if hander[0] == 1:
        filestring1 = "/Users/emersondetering/Downloads/BlackJackPython/png/ace_of_clubs.png"
    if hander[1] == 11:
        filestring2 = "/Users/emersondetering/Downloads/BlackJackPython/png/jack_of_clubs.png"
    if hander[1] == 12:
        filestring2 = "/Users/emersondetering/Downloads/BlackJackPython/png/queen_of_clubs.png"
    if hander[1] == 13:
        filestring2 = "/Users/emersondetering/Downloads/BlackJackPython/png/king_of_clubs.png"
    if hander[1] == 1:
        filestring2 = "/Users/emersondetering/Downloads/BlackJackPython/png/ace_of_clubs.png"

    image10 = Image.open(filestring1)  # put your own path here when running
    image20 = Image.open(filestring2)
    resized_image10 = image10.resize((110, 160), Image.Resampling.LANCZOS)
    resized_image20 = image20.resize((110, 160), Image.Resampling.LANCZOS)
    imageres10 = ImageTk.PhotoImage(resized_image10)
    imageres20 = ImageTk.PhotoImage(resized_image20)
    card_1.config(image=imageres10)
    card_2.config(image=imageres20)
    card_1.image=imageres10
    card_2.image=imageres20

diffic = None
def easy():
    global diffic
    diffic = "Easy"
    difeasy.config(state="pressed")
    difmedium.config(state="disabled")
    difhard.config(state="disabled")
def medium():
    global diffic
    diffic = "Medium"
    difmedium.config(state="pressed")
    difeasy.config(state="disabled")
    difhard.config(state="disabled")
def hard():
    global diffic
    diffic = "Hard"
    difhard.config(state="pressed")
    difmedium.config(state="disabled")
    difeasy.config(state="disabled")

# creating grid
for i in range(0, 4):
    win.columnconfigure(i, weight=2)
for i in range(0, 4):
    win.rowconfigure(i, weight=2)
for i in range(0, 4):
    stscreen.columnconfigure(i, weight=2)
for i in range(0, 4):
    stscreen.rowconfigure(i, weight=2)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=1)
# create card Images
image1 = Image.open(
    "/Users/emersondetering/Downloads/BlackJackPython/png/back.png")  # put your own path here when running
image2 = Image.open("/Users/emersondetering/Downloads/BlackJackPython/png/back.png")
resized_image1 = image1.resize((110, 160), Image.Resampling.LANCZOS)
resized_image2 = image2.resize((110, 160), Image.Resampling.LANCZOS)
imageres1 = ImageTk.PhotoImage(resized_image1)
imageres2 = ImageTk.PhotoImage(resized_image2)
# Create Cards
card_1 = Label(win, image=imageres1)
card_2 = Label(win, image=imageres2)
# Create buttons for main window
start = CircleButton(win, text="Start", command=establishround,borderless=1)
exit = CircleButton(win, text="Exit", command=quit,borderless=1)
deal = Button(win, text="Deal", command=deal,borderless=1,height = 50)

#create buttosn for start window
start = CircleButton(stscreen, text="Start", command=startgame,borderless=1)
difeasy = CircleButton(stscreen,text='Easy',command=easy,borderless=1)
difmedium = CircleButton(stscreen,text='Medium',command=medium,borderless=1)
difhard = CircleButton(stscreen,text='Hard',command=hard,borderless=1)
#create labels for main window
player = Label(win,text="Player",bg = '#35654d',font=('Times', 60, "bold"),fg='White');
dealer = Label(win,text="Dealer",bg = '#35654d',font=('Times', 60, "bold"),fg='White');

#labels for start window
wlcm = Label(stscreen,text="BlackJack Card Trainer",bg = '#35654d',font=('Times', 30, "bold"),fg='#000000')
sel = Label(stscreen,text="You need to select a difficulty",bg = '#35654d',font=('Times', 10, "bold"),fg='#000000')


# place buttons and labels on main
exit.grid(column=0, row=0,sticky = 'NW')
deal.grid(column=1, row=3, columnspan= 2)
card_1.grid(column=1, row=2)
card_2.grid(column=2, row=2)
player.grid(column=1,row = 1,columnspan= 2,sticky='S')
dealer.grid(column=1,row = 0,columnspan= 2,sticky='N')

#place buttons and labels on start screen
difeasy.grid(column=0,row=1)
difmedium.grid(column=1,row=1)
difhard.grid(column=2,row=1)
wlcm.grid(column=0,row=0,columnspan=3)
start.grid(column=1,row=2)
sel.grid(column=0,row=1,sticky='S',columnspan=3)
sel.grid_remove()
# key bindings
win.bind('<Escape>', lambda event: quit())

# Run window
stscreen.mainloop()
win.mainloop()
