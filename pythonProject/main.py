import random
from tkinter import *
from tkmacosx import Button
from tkmacosx import CircleButton  # used to change button colour
from PIL import ImageTk, Image


class Shoe:
    def __init__(self):
        self.Cards = []
        deck = []
        for x in range(1, 14):
            for y in range(0, 8):
                deck.append(x)
        self.Cards = deck


class Hand:
    def __init__(self):
        self.hand = []


class Round:
    def __init__(self):
        self.S = Shoe()
        self.Player = Hand()
        self.Dealer = Hand()
        self.count = 0

    def shuffle(self):
        random.shuffle(self.S.Cards)
        random.shuffle(self.S.Cards)
        random.shuffle(self.S.Cards)

    def newRound(self):
        self.Player.hand.clear()
        self.Dealer.hand.clear()
        self.hit("P")
        self.hit("P")
        self.hit("D")
        self.hit("D")

    def hit(self, user):
        if user == "P":
            card = self.S.Cards[0]
            if card >= 10:
                self.count -= 1
            elif card < 7:
                self.count += 1
            self.S.Cards.pop(0)
            self.Player.hand.append(card)
        elif user == "D":
            card = self.S.Cards[0]
            if card >= 10:
                self.count -= 1
            elif card < 7:
                self.count += 1
            self.S.Cards.pop(0)
            self.Dealer.hand.append(card)

    def value(self, user):
        handvalue = []
        hvalue = 0
        if user == "P":
            numcards = len(self.Player.hand)

            for x in range(0,numcards):
                if self.Player.hand[x]==1:
                    handvalue.append(11)
                elif self.Player.hand[x]==11 or self.Player.hand[x]==12 or self.Player.hand[x]==13:
                    handvalue.append(10)
                else:
                    handvalue.append(self.Player.hand[x])
            for x in range(0, numcards):
                if handvalue[x]==11 and sum(handvalue)>21:
                    handvalue[x]=1
            hvalue = sum(handvalue)
            return hvalue
        elif user == "D":
            numcards = len(self.Dealer.hand)

            for x in range(0, numcards):
                if self.Dealer.hand[x] == 1:
                    handvalue.append(11)
                elif self.Dealer.hand[x]==11 or self.Dealer.hand[x]==12 or self.Dealer.hand[x]==13:
                    handvalue.append(10)
                else:
                    handvalue.append(self.Dealer.hand[x])
            for x in range(0, numcards):
                if handvalue[x] == 11 and sum(handvalue)>21:
                    handvalue[x] = 1
            hvalue = sum(handvalue)
            return hvalue

    def win(self):
        if self.value("D") < self.value("P") <= 21:
            return 1  # Player wins
        elif self.value("P") < self.value("D") <= 21:
            return 2  # Dealer wins
        elif self.value("D") == self.value("P"):
            return 3  # push
        else:
            return 0  # no winner

    def check(self):
        if self.value("P") > 21:
            return 2  # Dealer wins
        elif self.value("P") == 21 and len(self.Player.hand) == 2:
            return 1  # Player wins, has Blackjack
        elif self.value("D") == 21:
            return 2  # Dealer has Blackjack
        else:
            return 0  # No winner yet

    def playerstand(self):
        while self.value("D") <= 21:
            if self.value("D") <= self.value("P") and self.value("D") < 17:
                card = self.S.Cards[0]
                if 1 < card < 7:
                    self.count += 1
                elif card >= 10 or card == 1:
                    self.count -= 1
                self.Dealer.hand.append(card)
                self.S.Cards.pop(0)
            elif self.value("D") >= 17:
                break
            else:
                break

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

    # if diffuclty hasnt been pressed, dont start game


def establishround():
    global R1
    start.config(text="Stop")
    R1 = Round()
    R1.shuffle()
    R1.newRound()
    # need code to establish round


def quit():
    # win.iconify()
    win.destroy()


global dealer_card_1

global dealer_card_2


def deal():
    R1.hit("P")
    R1.hit("P")
    R1.hit("D")
    R1.hit("D")
    hander = R1.Player.hand
    global card_1
    global card_2
    dealer_hand = R1.Dealer.hand


    filestring1 = "/Users/Charlabeast/Documents/BlackJackPython/png/" + str(hander[0]) + "_of_clubs.png"
    filestring2 = "/Users/Charlabeast/Documents/BlackJackPython/png/" + str(hander[1]) + "_of_clubs.png"
    if hander[0] == 11:
        filestring1 = "/Users/Charlabeast/Documents/BlackJackPython/png/jack_of_clubs.png"
    if hander[0] == 12:
        filestring1 = "/Users/Charlabeast/Documents/BlackJackPython/png/queen_of_clubs.png"
    if hander[0] == 13:
        filestring1 = "/Users/Charlabeast/Documents/BlackJackPython/png/king_of_clubs.png"
    if hander[0] == 1:
        filestring1 = "/Users/Charlabeast/Documents/BlackJackPython/png/ace_of_clubs.png"
    if hander[1] == 11:
        filestring2 = "/Users/Charlabeast/Documents/BlackJackPython/png/jack_of_clubs.png"
    if hander[1] == 12:
        filestring2 = "/Users/Charlabeast/Documents/BlackJackPython/png/queen_of_clubs.png"
    if hander[1] == 13:
        filestring2 = "/Users/Charlabeast/Documents/BlackJackPython/png/king_of_clubs.png"
    if hander[1] == 1:
        filestring2 = "/Users/Charlabeast/Documents/BlackJackPython/png/ace_of_clubs.png"

    image10 = Image.open(filestring1)  # put your own path here when running
    image20 = Image.open(filestring2)
    resized_image10 = image10.resize((110, 160), Image.Resampling.LANCZOS)
    resized_image20 = image20.resize((110, 160), Image.Resampling.LANCZOS)
    imageres10 = ImageTk.PhotoImage(resized_image10)
    imageres20 = ImageTk.PhotoImage(resized_image20)
    card_1.config(image=imageres10)
    card_2.config(image=imageres20)
    card_1.image = imageres10
    card_2.image = imageres20




    filestring3 = "/Users/Charlabeast/Documents/BlackJackPython/png/" + str(dealer_hand[0]) + "_of_clubs.png"
    filestring4 = "/Users/Charlabeast/Documents/BlackJackPython/png/back.png"
    if dealer_hand[0] == 11:
        filestring3 = "/Users/Charlabeast/Documents/BlackJackPython/png/jack_of_clubs.png"
    if dealer_hand[0] == 12:
        filestring3 = "/Users/Charlabeast/Documents/BlackJackPython/png/queen_of_clubs.png"
    if dealer_hand[0] == 13:
        filestring3 = "/Users/Charlabeast/Documents/BlackJackPython/png/king_of_clubs.png"
    if dealer_hand[0] == 1:
        filestring3 = "/Users/Charlabeast/Documents/BlackJackPython/png/ace_of_clubs.png"

    image30 = Image.open(filestring3)  # put your own path here when running
    image40 = Image.open(filestring4)
    resized_image30 = image30.resize((110, 160), Image.Resampling.LANCZOS)
    resized_image40 = image40.resize((110, 160), Image.Resampling.LANCZOS)
    imageres30 = ImageTk.PhotoImage(resized_image30)
    imageres40 = ImageTk.PhotoImage(resized_image40)
    dealer_card_1.config(image3=imageres30)
    dealer_card_2.config(image4=imageres40)
    dealer_card_1.image = imageres30
    dealer_card_2.image = imageres40





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
image1 = Image.open("/Users/Charlabeast/Documents/BlackJackPython/png/back.png")  # put your own path here when running
image2 = Image.open("/Users/Charlabeast/Documents/BlackJackPython/png/back.png")
image3 = Image.open("/Users/Charlabeast/Documents/BlackJackPython/png/back.png")
image4 = Image.open("/Users/Charlabeast/Documents/BlackJackPython/png/back.png")
resized_image1 = image1.resize((110, 160), Image.Resampling.LANCZOS)
resized_image2 = image2.resize((110, 160), Image.Resampling.LANCZOS)
resized_image3 = image1.resize((110, 160), Image.Resampling.LANCZOS)
resized_image4 = image1.resize((110, 160), Image.Resampling.LANCZOS)
imageres1 = ImageTk.PhotoImage(resized_image1)
imageres2 = ImageTk.PhotoImage(resized_image2)
imageres3 = ImageTk.PhotoImage(resized_image3)
imageres4 = ImageTk.PhotoImage(resized_image4)
# Create Cards
card_1 = Label(win, image=imageres1)
card_2 = Label(win, image=imageres2)
dealer_card_1 = Label(win, image=imageres3)
dealer_card_2 = Label(win, image=imageres4)
# Create buttons for main window
start = CircleButton(win, text="Start", command=establishround, borderless=1)
exit = CircleButton(win, text="Exit", command=quit, borderless=1)
deal = Button(win, text="Deal", command=deal, borderless=1, height=50)

# create buttosn for start window
start = CircleButton(stscreen, text="Start", command=startgame, borderless=1)
difeasy = CircleButton(stscreen, text='Easy', command=easy, borderless=1)
difmedium = CircleButton(stscreen, text='Medium', command=medium, borderless=1)
difhard = CircleButton(stscreen, text='Hard', command=hard, borderless=1)
# create labels for main window
player = Label(win, text="Player", bg='#35654d', font=('Times', 60, "bold"), fg='White');
dealer = Label(win, text="Dealer", bg='#35654d', font=('Times', 60, "bold"), fg='White');

# labels for start window
wlcm = Label(stscreen, text="BlackJack Card Trainer", bg='#35654d', font=('Times', 30, "bold"), fg='#000000')
sel = Label(stscreen, text="You need to select a difficulty", bg='#35654d', font=('Times', 10, "bold"), fg='#000000')

# place buttons and labels on main
exit.grid(column=0, row=0, sticky='NW')
deal.grid(column=1, row=3, columnspan=2)
card_1.grid(column=1, row=2)
card_2.grid(column=2, row=2)

dealer_card_1.grid(column=1, row=1)
dealer_card_2.grid(column=2, row=1)
player.grid(column=1,row = 1,columnspan= 2,sticky='S')
dealer.grid(column=1,row = 0,columnspan= 2,sticky='N')

#place buttons and labels on start screen
difeasy.grid(column=0,row=1)
difmedium.grid(column=1,row=1)
difhard.grid(column=2,row=1)
wlcm.grid(column=0,row=0,columnspan=3)
start.grid(column=1,row=2)
sel.grid(column=0,row=1,sticky='S',columnspan=3)

player.grid(column=1, row=1, columnspan=2, sticky='S')
dealer.grid(column=1, row=0, columnspan=2, sticky='N')

# place buttons and labels on start screen
difeasy.grid(column=0, row=1)
difmedium.grid(column=1, row=1)
difhard.grid(column=2, row=1)
wlcm.grid(column=0, row=0, columnspan=3)
start.grid(column=1, row=2)
sel.grid(column=0, row=1, sticky='S', columnspan=3)

sel.grid_remove()
# key bindings
win.bind('<Escape>', lambda event: quit())

# Run window
stscreen.mainloop()
win.mainloop()
