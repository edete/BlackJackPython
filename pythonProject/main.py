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
from tkmacosx import Button  # used to change button colour
from PIL import ImageTk, Image

# Import tkinter library

# Create an instance of Tkinter frame or window
win = Tk()

# Set the geometry of tkinter frame
win.geometry("400x300")


# establish commands
def establishround():
    global R1
    btn.config(text="Stop Game")
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
    resized_image10 = image10.resize((55, 80), Image.Resampling.LANCZOS)
    resized_image20 = image20.resize((55, 80), Image.Resampling.LANCZOS)
    imageres10 = ImageTk.PhotoImage(resized_image10)
    imageres20 = ImageTk.PhotoImage(resized_image20)
    card_1.config(image=imageres10)
    card_2.config(image=imageres20)
    card_1.image=imageres10
    card_2.image=imageres20


# creating grid
for i in range(0, 4):
    win.columnconfigure(i, weight=2)
for i in range(0, 4):
    win.rowconfigure(i, weight=2)

win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=1)
# create card Images
image1 = Image.open(
    "/Users/emersondetering/Downloads/BlackJackPython/png/2_of_clubs.png")  # put your own path here when running
image2 = Image.open("/Users/emersondetering/Downloads/BlackJackPython/png/7_of_clubs.png")
resized_image1 = image1.resize((55, 80), Image.Resampling.LANCZOS)
resized_image2 = image2.resize((55, 80), Image.Resampling.LANCZOS)
imageres1 = ImageTk.PhotoImage(resized_image1)
imageres2 = ImageTk.PhotoImage(resized_image2)
# Create Cards
card_1 = Label(win, image=imageres1)
card_2 = Label(win, image=imageres2)
# Create buttons
btn = Button(win, text="Start Game", command=establishround)
exit = Button(win, text="Exit Game", command=quit)
deal = Button(win, text="Deal", command=deal)

# place buttons
exit.grid(column=0, row=0, sticky="EW")
btn.grid(column=1, row=3, sticky="EW")
deal.grid(column=3, row=0, sticky="EW")
card_1.grid(column=1, row=2)
card_2.grid(column=2, row=2)
# key bindings
win.bind('<Escape>', lambda event: quit())

# Run window
win.mainloop()
