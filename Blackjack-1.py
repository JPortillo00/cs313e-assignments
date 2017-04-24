#  File: Blackjack.py
#  Description: PLay BlackJack
#  Student's Name: Jairo Portillo
#  Student's UT EID: jeo2896
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created:9/18/2016
#  Date Last Modified:9/22/2016

class Player:
    
    def __init__(self):
        self.hand = []
        self.handTotal = 0
    
    def __str__(self):
        text = ""
        for i in range(0,len(self.hand)):
            text += " " + str(self.hand[i])           
        return text

class Card:

    def __init__(self,suit,pip,value):
        self.suit = suit
        self.pip = pip
        self.value = value

    def __int__(self):
        return self.value

    def __str__(self):
        return (self.pip + self.suit)


class Deck:

    def __init__(self):
        suits = ["C", "D", "H", "S"]
        values = list(range(2,11))
        self.cardList = [''] * 52
        for s in range(0,4):
            for c in range(0,13):                
                if (c+1)%10==0 :
                    self.cardList[c+13*s] = Card(suits[s],"J",10)
                elif (c+1)%11==0 :
                    self.cardList[c+13*s] = Card(suits[s],"Q",10)
                elif (c+1)%12==0 :
                    self.cardList[c+13*s] = Card(suits[s],"K",10)
                elif (c+1)%13==0 :
                    self.cardList[c+13*s] = Card(suits[s],"A",11)
                else:
                    self.cardList[c+13*s] = Card(suits[s],str(values[c]),values[c])
                                
    def shuffle(self):
        import random
        random.shuffle(self.cardList)

    def dealOne(self,player):
        player.hand.append(self.cardList.pop(0))
        
    def __str__(self):
        text = ""
        for i in range(0,len(self.cardList)):
            if (i+1)%13 == 0:
                text += "  " + str(self.cardList[i]) + "\n"
            elif self.cardList[i].pip == "10":
                text += " " + str(self.cardList[i])
            else:
                text += "  " + str(self.cardList[i])
        return text
        

def playerTurn(deck,dealer,opponent):
    print("\nThe House gives the challenger the first move.\n")

    if opponent.hand[0].value == 11 or opponent.hand[1].value == 11:
        print("Assuming 11 points for an ace you were dealt for now")        
    opponent.handTotal += int(opponent.hand[0]) + int(opponent.hand[1])
    print("You hold " + str(opponent.hand[0]) + " " + str(opponent.hand[1]) + " for a total of " + str(opponent.handTotal))

    if opponent.handTotal > 21 and opponent.hand[0].value == 11:
        print("Over 21. Switching an ace from 11 points to 1.")
        opponent.hand[0].value = 1
        opponent.handTotal -= 10
        print("New Total: " + str(opponent.handTotal))
    elif opponent.handTotal > 21 and opponent.hand[1].value == 11:
        print("Over 21. Switching an ace from 11 points to 1.")
        opponent.hand[1].value = 1
        opponent.handTotal -= 10
        print("New Total: " + str(opponent.handTotal) + "\n")

    user = int(input("1 (hit) or 2 (stay)? "))

    i = 1 #counter for added cards
    while opponent.handTotal < 21 and user != 2:
        i+=1
        deck.dealOne(opponent)
        print("\nCard Dealt: " + str(opponent.hand[i]))
        opponent.handTotal += int(opponent.hand[i])
        if opponent.hand[i].value == 11:
            print("Assuming 11 points for an ace you were dealt for now")  

        for x in range(0,len(opponent.hand)):
            if opponent.handTotal > 21 and opponent.hand[x].value == 11:
                print("Over 21. Switching an ace from 11 points to 1.")
                opponent.hand[x].value = 1
                opponent.handTotal -= 10                
        print("New Total: " + str(opponent.handTotal) + "\n")
        if opponent.handTotal >= 21:
            user = 2
        else:
            print("You hold " + str(opponent) + " for a total of " + str(opponent.handTotal) + ".")
            user = int(input("1 (hit) or 2 (stay)?"))
            
    if opponent.handTotal > 21:
        print("\nYou hold" + str(opponent) + " for a total of " + str(opponent.handTotal) + ".")
        print("BUST! YOU LOSE!")
    elif opponent.handTotal == 21:
        print("\nYou hold" + str(opponent) + " for a total of " + str(opponent.handTotal) + ".")
        print("BLACKJACK! YOU WIN! For now....")
    else:
        print("\nYou hold" + str(opponent) + " for a total of " + str(opponent.handTotal) + ".")
        print("You stay with " + str(opponent.handTotal) + ".")

        

def dealerTurn(deck,dealer,opponent):
    print("\nDealer's Turn\n")
    print("Your hand:" + str(opponent) + " for a total of "+ str(opponent.handTotal))
    dealer.handTotal += int(dealer.hand[0]) + int(dealer.hand[1])
    print("Dealer's hand:" + str(dealer) + " for a total of "+ str(dealer.handTotal))
    if dealer.hand[0].value == 11 or dealer.hand[1].value == 11:
        print("Assuming 11 points for an ace you were dealt for now\n")  
    if dealer.handTotal > 21 and dealer.hand[0].value == 11:
        print("Over 21. Switching an ace from 11 points to 1.")
        dealer.hand[0].value = 1
        dealer.handTotal -= 10
        print("New Total: " + str(dealer.handTotal))
    elif dealer.handTotal > 21 and dealer.hand[1].value == 11:
        print("Over 21. Switching an ace from 11 points to 1.")
        dealer.hand[1].value = 1
        dealer.handTotal -= 10
        print("New Total: " + str(dealer.handTotal) + "\n")
    if len(opponent.hand) == 2 and opponent.handTotal == 21:
       print("\nDealer holds" + str(dealer) + " for a total of " + str(dealer.handTotal) + ".")
       print("THE HOUSE LOSES! YOU WIN...")
    else:
        i = 1
        user = 1
        while opponent.handTotal > dealer.handTotal and user != 2:
            i+=1
            deck.dealOne(dealer)
            print("\nCard Dealt: " + str(dealer.hand[i]))
            dealer.handTotal += int(dealer.hand[i])
            if dealer.hand[i].value == 11:
                print("Assuming 11 points for an ace you were dealt for now")
            for x in range(0,len(dealer.hand)):
                if dealer.handTotal > 21 and dealer.hand[x].value == 11:
                    print("Over 21. Switching an ace from 11 points to 1.")
                    dealer.hand[x].value = 1
                    dealer.handTotal -= 10                
            print("New Total: " + str(dealer.handTotal) + "\n")
            if dealer.handTotal >= 21:
                user = 2
            else:
                user = 1

        if opponent.handTotal <= 21:
            if dealer.handTotal > 21:
                print("\nDealer holds" + str(dealer) + " for a total of " + str(dealer.handTotal) + ".")
                print("DEALER BUSTS! YOU WIN...")
            elif dealer.handTotal == 21:
                print("\nDealer holds" + str(dealer) + " for a total of " + str(dealer.handTotal) + ".")
                print("BLACKJACK! THE HOUSE WINS! YOU LOSE!")
            elif dealer.handTotal == opponent.handTotal:
                print("\nDealer holds" + str(dealer) + " for a total of " + str(dealer.handTotal) + ".")
                print("THE HOUSE WINS! YOU LOSE!")
            elif dealer.handTotal < opponent.handTotal:
                print("\nDealer holds" + str(dealer) + " for a total of " + str(dealer.handTotal) + ".")
                print("THE HOUSE LOSES! YOU WIN...")
            else:
                print("\nDealer holds" + str(dealer) + " for a total of " + str(dealer.handTotal) + ".")
                print("THE HOUSE WINS! YOU LOSE!")
        else:
            print("\nDealer holds" + str(dealer) + " for a total of " + str(dealer.handTotal) + ".")
            print("YOU BUSTED! THE HOUSE WINS!")

      
    
        
        

def main():
    import random

    print("Initial Deck:")
    cardDeck = Deck()
    print(cardDeck)

    print("Shuffled Deck:")
    #random.seed(50)
    cardDeck.shuffle()
    print(cardDeck)

    dealer = Player()
    opponent = Player()

    
    cardDeck.dealOne(opponent)      
    cardDeck.dealOne(dealer)        
    cardDeck.dealOne(opponent)      
    cardDeck.dealOne(dealer)        

    print("Deck after dealing two cards each:")
    print(cardDeck)

    
    print("Dealer shows " + str(dealer.hand[1]) + " faceup.")
    print("You show " + str(opponent.hand[1]) + " faceup.")

    playerTurn(cardDeck,dealer,opponent)
    dealerTurn(cardDeck,dealer,opponent)

    print("\nGamer Over.")
    print("Final hands and Totals:")
    print("\tDealer: " + str(dealer))
    print("\tTotal: " + str(dealer.handTotal))
    print("\tOpponent: " + str(opponent))
    print("\tTotal: " + str(opponent.handTotal))
    
main()
        
