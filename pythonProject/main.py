import random
import time
from tkinter import *
from tkmacosx import Button
from tkmacosx import CircleButton  # used to change button colour
from PIL import ImageTk, Image
import ast

#Deck class
class Shoe:
    def __init__(self):
        self.Cards = []
        deck = []
        for x in range(1, 14):
            for y in range(0, 16):
                deck.append(x)
        self.Cards = deck

#Hand class
class Hand:
    def __init__(self):
        self.hand = []

#Round class
class Round:
    def __init__(self):
        self.S = Shoe()
        self.Player = Hand()
        self.Dealer = Hand()
        self.count = 0

    #Shuffle function that randomizes cards
    def shuffle(self):
        random.shuffle(self.S.Cards)
        random.shuffle(self.S.Cards)
        random.shuffle(self.S.Cards)

    #New round function that clears the previous hands
    def newRound(self):
        self.Player.hand.clear()
        self.Dealer.hand.clear()
        self.hit("P")
        self.hit("P")
        self.hit("D")
        self.hit("D")

    #Hit function that adds a card to the users hand
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

    #Assigns numeric value to the cards in users and dealers hand
    def value(self, user):
        handvalue = []
        hvalue = 0
        #Users hand
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
        #Dealers hand
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

    #Win function, determines who wins
    def win(self):
        if self.value("D") < self.value("P") <= 21:
            return 1  # Player wins
        elif self.value("P") < self.value("D") <= 21:
            return 2  # Dealer wins
        elif self.value("D") == self.value("P"):
            return 3  # push
        elif self.value("D") > 21:
            return 1
        else:
            return 0  # no winner

    def check(self):
        if self.value("P") > 21:
            return 2  # Dealer wins
        elif self.value("P") == 21 and len(self.Player.hand) == 2:
            return 1  # Player wins, has Blackjack
        elif self.value("D") == 21:
            return 3  # Dealer has Blackjack
        elif self.value("D") == self.value("P"):
            return 4
        else:
            return 0  # No winner yet

    #Stand function that keeps hand as is and adjusts card count as necessary
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
stscreen = Tk()
# Set the geometry of tkinter frame
stscreen.geometry("500x500")
win.geometry("1200x900")
#Set background color
win.config(background='#35654d')
stscreen.config(background='#35654d')
#Keep main window hidden until difficulty is selected
win.withdraw()
#Place window in the center of the screen
stscreen.eval('tk::PlaceWindow . center')

#positions of cards
poscard1 = 0.4
poscard2 = 0.5

poscard1d = 0.4
poscard2d = 0.5
#hit card counter
counter = 2



a=0

#read card counter answer from user
def readanswer():
    global correct
    global incorrect
    global invalid
    global a
    answer = userinput.get()


    if answer.lstrip('-').isnumeric(): #This is so that if input is negative it works
        if a == 2:
            invalid.destroy()
        elif a == 1:
            incorrect.destroy()

        if int(answer.lstrip('-')) == R1.count:
                #Display if the users card count is correct
                a=3
                print('correct')
                correct=Label(win, text="You are correct", bg='#35654d', font=('Times', 20, 'bold'), fg='White')
                correct.grid(column=3, row=2)
                userinput.delete(0,'end')


        elif int(answer.lstrip('-')) != R1.count:
                # Display if the users card count is incorrect
                print('You are incorrect')
                a=1
                incorrect=Label(win, text="You are incorrect", bg='#35654d', font=('Times', 20, 'bold'), fg='White')
                incorrect.grid(column=3, row=2)
                userinput.delete(0,'end')



    else:
        #Display the users card count input is invalid
        print('invalid')
        a=2
        invalid=Label(win, text="Please enter an integer", bg='#35654d', font=('Times', 20, 'bold'), fg='White')
        invalid.grid(column=3, row=2)
        userinput.delete(0,'end')



# establish commands
def startgame():
    global diffcounter
    diffcounter = 0
    #If the difficulty hasn't been selected, don't start the game
    if diffic != None:
        diffcounter = 0
        stscreen.destroy()
        win.deiconify()
    else:
        sel.grid()


#Function to reveal the second dealer card
def showdealersecond():
    secondcardvalue = R1.Dealer.hand[1]
    filestringsecond = "/Users/hussain/Downloads/BlackJackPython/png/" + str(
        secondcardvalue) + "_of_clubs.png"
    if secondcardvalue == 11:
        filestringsecond = "/Users/hussain/Downloads/BlackJackPython/png/jack_of_clubs.png"
    if secondcardvalue == 12:
        filestringsecond = "/Users/hussain/Downloads/BlackJackPython/png/queen_of_clubs.png"
    if secondcardvalue == 13:
        filestringsecond = "/Users/hussain/Downloads/BlackJackPython/png/king_of_clubs.png"
    if secondcardvalue == 1:
        filestringsecond = "/Users/hussain/Downloads/BlackJackPython/png/ace_of_clubs.png"
    imagesecond = Image.open(filestringsecond)  # put your own path here when running
    resized_imagesecond = imagesecond.resize((110, 160), Image.Resampling.LANCZOS)
    imageressecond = ImageTk.PhotoImage(resized_imagesecond)
    dealer_card_2.config(image=imageressecond)
    dealer_card_2.image = imageressecond


global R1
R1 = Round()
R1.shuffle()
diffic = None

#Exit function
def quit():
    # win.iconify()
    win.destroy()

#Dealer card functions
global dealer_card_1
global dealer_card_2


#Deal function
def deal():
    deal.config(state = "disabled")
    global card_1
    global card_2
    global counter
    global diffcounter
    diffcounter = diffcounter + 1
    stand.config(state = "normal")
    hitter.config(state = "normal")
    winner.grid_remove()
    player.grid()
    userinput.grid_remove()
    counter = 2

#resetting the board
    for j in cardlist:
        j.destroy()

    for j in dealercardlist:
        j.destroy()

#Resets correct message
    if a==3:
        correct.destroy()

#Resets cards
    cardlist.clear()
    dealercardlist.clear()

    #Position of the cards
    global poscard1
    poscard1  = 0.4
    global poscard2
    poscard2 = 0.5
    global poscard1d
    poscard1d = 0.4
    global poscard2d
    poscard2d = 0.5
    card_1.place(relx=poscard1, rely=0.6)
    card_2.place(relx=poscard2, rely=0.6)
    dealer_card_1.place(relx=poscard1, rely=0.15)
    dealer_card_2.place(relx=poscard2, rely=0.15)

    global hander
    R1.newRound()
    R1.shuffle()
    hander = R1.Player.hand
    dealer_hand = R1.Dealer.hand

#Assigning appropriate images to card values
    if hander[0] == 11:
        filestring1 = "/Users/hussain/Downloads/BlackJackPython/png/jack_of_clubs.png"
    elif hander[0] == 12:
        filestring1 = "/Users/hussain/Downloads/BlackJackPython/png/queen_of_clubs.png"
    elif hander[0] == 13:
        filestring1 = "/Users/hussain/Downloads/BlackJackPython/png/king_of_clubs.png"
    elif hander[0] == 1:
        filestring1 = "/Users/hussain/Downloads/BlackJackPython/png/ace_of_clubs.png"
    else:
        filestring1 = "/Users/hussain/Downloads/BlackJackPython/png/" + str(hander[0]) + "_of_clubs.png"

    if hander[1] == 11:
        filestring2 = "/Users/hussain/Downloads/BlackJackPython/png/jack_of_clubs.png"
    elif hander[1] == 12:
        filestring2 = "/Users/hussain/Downloads/BlackJackPython/png/queen_of_clubs.png"
    elif hander[1] == 13:
        filestring2 = "/Users/hussain/Downloads/BlackJackPython/png/king_of_clubs.png"
    elif hander[1] == 1:
        filestring2 = "/Users/hussain/Downloads/BlackJackPython/png/ace_of_clubs.png"
    else:
        filestring2 = "/Users/hussain/Downloads/BlackJackPython/png/" + str(hander[1]) + "_of_clubs.png"

#Read user card images in, resize them appropriately, and display them
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
    print(hander)
    print(dealer_hand)

# Read dealer images in, resize them appropriately, and display them
    filestring3 = "/Users/hussain/Downloads/BlackJackPython/png/" + str(dealer_hand[0]) + "_of_clubs.png"
    filestring4 = "/Users/hussain/Downloads/BlackJackPython/png/back.png"
    if dealer_hand[0] == 11:
        filestring3 = "/Users/hussain/Downloads/BlackJackPython/png/jack_of_clubs.png"
    if dealer_hand[0] == 12:
        filestring3 = "/Users/hussain/Downloads/BlackJackPython/png/queen_of_clubs.png"
    if dealer_hand[0] == 13:
        filestring3 = "/Users/hussain/Downloads/BlackJackPython/png/king_of_clubs.png"
    if dealer_hand[0] == 1:
        filestring3 = "/Users/hussain/Downloads/BlackJackPython/png/ace_of_clubs.png"

    image30 = Image.open(filestring3)  #put your own path here when running
    image40 = Image.open(filestring4)
    resized_image30 = image30.resize((110, 160), Image.Resampling.LANCZOS)
    resized_image40 = image40.resize((110, 160), Image.Resampling.LANCZOS)
    imageres30 = ImageTk.PhotoImage(resized_image30)
    imageres40 = ImageTk.PhotoImage(resized_image40)
    dealer_card_1.config(image=imageres30)
    dealer_card_2.config(image=imageres40)
    dealer_card_1.image = imageres30
    dealer_card_2.image = imageres40

    cardcount.set(R1.count)

    w = R1.check()
#Set possible messages for the appropriate winning outcomes and disable the hit and stand buttons
    if w == 2:
        winnervar.set("Dealer wins")
        winner.grid()
        player.grid_remove()
        stand.config(state="disabled")
        hitter.config(state="disabled")
        deal.config(state ="normal")
        showdealersecond()
        if diffcounter == threshold:
            userinput.grid()
            userinput.delete(0, 'end')
            #readanswer()
    elif w == 3:
        winnervar.set("Blackjack! Dealer wins!")
        winner.grid()
        player.grid_remove()
        stand.config(state="disabled")
        hitter.config(state="disabled")
        deal.config(state="normal")
        showdealersecond()
        if diffcounter == threshold:
            userinput.grid()
            userinput.delete(0, 'end')
            #readanswer()
    elif w == 4:
        winnervar.set("You both have Blackjack! Push!")
        winner.grid()
        player.grid_remove()
        stand.config(state="disabled")
        hitter.config(state="disabled")
        deal.config(state="normal")
        showdealersecond()
        if diffcounter == threshold:
            userinput.grid()
            userinput.delete(0, 'end')
            #readanswer()

global cardlist
global dealercardlist
# creating label list of cards to add them dynamically
cardlist = []
dealercardlist = []

#Hit function
def hit():

    global counter
    global poscard1
    global poscard2
    #User hit
    R1.hit("P")
    cardvalue = hander[counter]
    #Assign appropriate card images for the card values
    filestringhit= "/Users/hussain/Downloads/BlackJackPython/png/" + str(cardvalue) + "_of_clubs.png"
    if cardvalue == 11:
        filestringhit = "/Users/hussain/Downloads/BlackJackPython/png/jack_of_clubs.png"
    if cardvalue == 12:
        filestringhit = "/Users/hussain/Downloads/BlackJackPython/png/queen_of_clubs.png"
    if cardvalue == 13:
        filestringhit = "/Users/hussain/Downloads/BlackJackPython/png/king_of_clubs.png"
    if cardvalue == 1:
        filestringhit = "/Users/hussain/Downloads/BlackJackPython/png/ace_of_clubs.png"

#Display card images for the user
    imagehit = Image.open(filestringhit)  # put your own path here when running
    resized_imagehit = imagehit.resize((110, 160), Image.Resampling.LANCZOS)
    imagereshit = ImageTk.PhotoImage(resized_imagehit)
    hitcard = Label(win, image=imagereshit)
    hitcard.image = imagereshit

#Apply shift to make room for the additional cards
    shift = 0.05*(counter-1)

    poscard1 = (poscard1 - 0.1)
    poscard2 = (poscard2 - 0.1)

    hitcard.place(rely=0.6,relx = 0.5 + shift)
    card_1.place(rely=0.6,relx=(poscard1 + shift))
    card_2.place(rely=0.6,relx=(poscard2 + shift))
    if counter > 2:
        for j in range (0,len(cardlist)):
            cardlist[j].place(rely = 0.6, relx = ((poscard2 + 0.1)+(j * 0.1) + shift))
    cardlist.append(hitcard)
#Update card count variable
    counter = counter + 1
    cardcount.set(R1.count)
    w = R1.check()

# Set possible messages for the appropriate winning outcomes and disable the hit and stand buttons
    if w == 1:
        #User wins
        winnervar.set("You win!")
        winner.grid()
        player.grid_remove()
        stand.config(state="disabled")
        hitter.config(state="disabled")
        deal.config(state="normal")
        showdealersecond()
        if diffcounter == threshold:
            userinput.delete(0, 'end')
            userinput.grid()
            #readanswer()
    if w == 2:
        #Dealer wins
        winnervar.set("Dealer wins")
        winner.grid()
        player.grid_remove()
        stand.config(state="disabled")
        hitter.config(state="disabled")
        deal.config(state="normal")
        showdealersecond()
        if diffcounter == threshold:
            userinput.delete(0, 'end')
            userinput.grid()
            #readanswer()
    elif w == 3:
        #Dealer gets blackjack and wins
        winnervar.set("Blackjack! Dealer wins!")
        winner.grid()
        player.grid_remove()
        stand.config(state="disabled")
        hitter.config(state="disabled")
        deal.config(state="normal")
        showdealersecond()
        if diffcounter == threshold:
            userinput.delete(0, 'end')
            userinput.grid()
            #readanswer()

#Stand function for when user wants to keep the cards they have
def stand():

    global poscard2d
    global poscard1d
    R1.playerstand()
    handsize = len(R1.Dealer.hand)

#Assign card value and image for the dealers second card
    secondcardvalue = R1.Dealer.hand[1]
    filestringsecond = "/Users/hussain/Downloads/BlackJackPython/png/" + str(secondcardvalue) + "_of_clubs.png"
    if secondcardvalue == 11:
        filestringsecond = "/Users/hussain/Downloads/BlackJackPython/png/jack_of_clubs.png"
    if secondcardvalue == 12:
        filestringsecond = "/Users/hussain/Downloads/BlackJackPython/png/queen_of_clubs.png"
    if secondcardvalue == 13:
        filestringsecond = "/Users/hussain/Downloads/BlackJackPython/png/king_of_clubs.png"
    if secondcardvalue == 1:
        filestringsecond = "/Users/hussain/Downloads/BlackJackPython/png/ace_of_clubs.png"
#Resize and display dealers second card
    imagesecond = Image.open(filestringsecond)  # put your own path here when running
    resized_imagesecond = imagesecond.resize((110, 160), Image.Resampling.LANCZOS)
    imageressecond = ImageTk.PhotoImage(resized_imagesecond)
    dealer_card_2.config(image=imageressecond)
    dealer_card_2.image = imageressecond

#Adding cards if dealer hits
    for x in range(2, handsize):
        cardvalue = R1.Dealer.hand[x]
        filestringhit = "/Users/hussain/Downloads/BlackJackPython/png/" + str(cardvalue) + "_of_clubs.png"
        if cardvalue == 11:
            filestringhit = "/Users/hussain/Downloads/BlackJackPython/png/jack_of_clubs.png"
        if cardvalue == 12:
            filestringhit = "/Users/hussain/Downloads/BlackJackPython/png/queen_of_clubs.png"
        if cardvalue == 13:
            filestringhit = "/Users/hussain/Downloads/BlackJackPython/png/king_of_clubs.png"
        if cardvalue == 1:
            filestringhit = "/Users/hussain/Downloads/BlackJackPython/png/ace_of_clubs.png"
        imagehit = Image.open(filestringhit)  # put your own path here when running
        resized_imagehit = imagehit.resize((110, 160), Image.Resampling.LANCZOS)
        imagereshit = ImageTk.PhotoImage(resized_imagehit)
        hitcard = Label(win, image=imagereshit)
        hitcard.image = imagereshit

#Applying shift for additional cards
        shift = 0.05 * (x-1)

        poscard1d = (poscard1d - 0.1)
        poscard2d = (poscard2d - 0.1)

        hitcard.place(rely=0.15, relx=0.5 + shift)
        dealer_card_1.place(rely=0.15, relx=(poscard1d + shift))
        dealer_card_2.place(rely=0.15, relx=(poscard2d + shift))
        if x > 1:
            for j in range(0, len(dealercardlist)):
                dealercardlist[j].place(rely=0.15, relx=((poscard2d + 0.1) + (j * 0.1) + shift))
        dealercardlist.append(hitcard)
#Winning outcomes
    w = R1.win()
    #User wins
    if w == 1:
        winnervar.set("You win")
        winner.grid()
        player.grid_remove()
        #Disable stand and hit buttons
        stand.config(state="disabled")
        hitter.config(state="disabled")
        #Keep deal button
        deal.config(state="normal")
        showdealersecond()
        if diffcounter == threshold:
            userinput.grid()
            userinput.delete(0, 'end')
            #readanswer()
    #Dealer wins
    elif w == 2:
        winnervar.set("Dealer wins")
        winner.grid()
        player.grid_remove()
        # Disable stand and hit buttons
        stand.config(state="disabled")
        hitter.config(state="disabled")
        deal.config(state="normal")
        showdealersecond()
        if diffcounter == threshold:
            userinput.grid()
            userinput.delete(0, 'end')
            #readanswer()
    #Push (i.e. a tie), no one wins
    elif w == 3:
        winnervar.set("Push")
        winner.grid()
        player.grid_remove()
        stand.config(state="disabled")
        hitter.config(state="disabled")
        deal.config(state="normal")
        showdealersecond()
        if diffcounter == threshold:
            userinput.grid()
            userinput.delete(0, 'end')
            #readanswer()

global diffcounter
global threshold

#Difficlty Functions
#Easy Difficulty, asks for card count every 4 rounds
def easy():
    global diffic
    global threshold
    diffic = "Easy"
    difeasy.config(state="pressed")
    difmedium.config(state="disabled")
    difhard.config(state="disabled")
    threshold = 4

#Medium Difficulty, asks for card count every 6 rounds
def medium():
    global diffic
    global threshold
    diffic = "Medium"
    difmedium.config(state="pressed")
    difeasy.config(state="disabled")
    difhard.config(state="disabled")
    threshold = 6

#Hard Difficulty, asks for difficulty every 8 rounds
def hard():
    global diffic
    global threshold
    diffic = "Hard"
    difhard.config(state="pressed")
    difmedium.config(state="disabled")
    difeasy.config(state="disabled")
    threshold = 8


# Create grid to place all the buttons and card images
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

# Read in and resize back of card images for initial main window
image1 = Image.open("/Users/hussain/Downloads/BlackJackPython/png/back.png")  # put your own path here when running
image2 = Image.open("/Users/hussain/Downloads/BlackJackPython/png/back.png")
image3 = Image.open("/Users/hussain/Downloads/BlackJackPython/png/back.png")
image4 = Image.open("/Users/hussain/Downloads/BlackJackPython/png/back.png")
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

# Create exit, deal, hit, and stand buttons for the main window
exit = CircleButton(win, text="Exit", command=quit, borderless=1)
deal = Button(win, text="Deal", command=deal, borderless=1, height=50)
hitter = Button(win, text="Hit", command=hit, borderless=1, height=50)
stand = Button(win, text="Stand", command=stand, borderless=1, height=50)

# create start, how to play, and the difficulty for the start window
start = CircleButton(stscreen, text="Start", command=startgame, borderless=1)
difeasy = CircleButton(stscreen, text='Easy', command=easy, borderless=1)
difmedium = CircleButton(stscreen, text='Medium', command=medium, borderless=1)
difhard = CircleButton(stscreen, text='Hard', command=hard, borderless=1)

#Create card counter and the user input box for counting
cardcount = IntVar(win, R1.count)
winnervar = StringVar(win, "")

#Create labels for the main window
player = Label(win, text="Player", bg='#35654d', font=('Times', 40, "bold"), fg='White')
dealer = Label(win, text="Dealer", bg='#35654d', font=('Times', 40, "bold"), fg='White')
countlab = Label(win, text = "Card Count", bg = '#35654d', font=('Times', 20, "bold"), fg = 'White')
counting = Label(win, textvariable = cardcount)
winner = Label(win, textvariable = winnervar, bg='#35654d', font=('Times', 60, "bold"), fg='White')


#Create labels for the start window
wlcm = Label(stscreen, text="Blackjack Card Counting Trainer", bg='#35654d', font=('Times', 24, "bold"), fg='White')
sel = Label(stscreen, text="Select a difficulty", bg='#35654d', font=('Times', 10, "bold"), fg='#000000')

#Place buttons, labels and cards on the main window
exit.grid(column=0, row=0, sticky='NW')
deal.grid(column=3, row=0, sticky='NE')
stand.grid(column=2, row=3)
card_1.place(relx=poscard1,rely=0.6)
card_2.place(relx=poscard2,rely=0.6)
hitter.grid(column=1, row=3)
counting.grid(column=0,row=1,columnspan=2)

dealer_card_1.place(relx=poscard1d,rely=0.15)
dealer_card_2.place(relx=poscard2d,rely=0.15)
player.grid(column=1,row = 1,columnspan= 2)
dealer.grid(column=1,row = 0,columnspan= 2,sticky='N')
winner.grid(column=1,row = 1,columnspan= 2)
countlab.grid(column=0, row=1, columnspan=1)
winner.grid_remove()

#place buttons and labels on the start screen
difeasy.grid(column=0,row=1)
difmedium.grid(column=1,row=1)
difhard.grid(column=2,row=1)
wlcm.grid(column=0,row=0,columnspan=3)
start.grid(column=1,row=2)
sel.grid(column=0,row=1,sticky='S',columnspan=3)

#Create user input for count
userinputLabel = Label(win, text = "Enter Your Card Count", bg = '#35654d', font=('Times', 20, "bold"), fg = 'White')
userinputLabel.grid(column=3,row=0,columnspan=1)
userinput = Entry(win)
userinput.focus_set()
userinput.grid(column=3,row=1,columnspan=1)
userinput.grid_remove()

sel.grid_remove()

#Key bindings
win.bind('<Escape>', lambda event: quit())
win.bind('<Return>', lambda event: readanswer())

#Run window
stscreen.mainloop()
win.mainloop()