import random
playerIn = True
dealerIn = True

deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A']
player1 = []
dealer = []
pay = 0

def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total = 0
    faceCard = ['J','K','Q']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in faceCard:
            total +=10
        else:
            if total > 11:
                total += 1
            else:
                total +=11

    return total

def dealerShowsHand():
     if len(dealer) == 2:
         return dealer[0]
     elif len(dealer)>2:
         return dealer[0],dealer[1]


for _ in range(2):
    dealCard(dealer)
    dealCard(player1)

#print("Table min $10")
#pay = int(input("How much would you like to bet!\nNo greater than $100: "))
#while pay > 0 and pay < 101:

#    print("")
#    end = input("Quit at anytime will end game\nwould you like to continue!:")
#   print("")

#    if(end.lower() == "quit"):
        #break


while playerIn or dealerIn:


    print(f"Dealer has {dealerShowsHand()} and X")
    print(f"You have {player1} for a total of {total(player1)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealer) > 16:
        dealerIn = False
    else:
        dealCard(dealer)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(player1)
    if total(player1)>= 21:
        break
    elif total(dealer) >= 21:
        break
if total(player1) == 21:
    print(f"\nYou have{player1} for a total of {total(player1)} and the dealer has{dealer} for a total of {total(dealer)}")
    print("Blackjack!")
elif total(dealer) ==21:
    print(f"\nYou have{player1} for a total of {total(player1)} and the dealer has{dealer} for a total of {total(dealer)}")
    print("You lose!")
elif total(player1) > 21:
    print(f"\nYou have{player1} for a total of {total(player1)} and the dealer has{dealer} for a total of {total(dealer)}")
    print("Bust!")
elif total(dealer) > 21:
    print(f"\nYou have{player1} for a total of {total(player1)} and the dealer has{dealer} for a total of {total(dealer)}")
    print("Dealer bust!")
elif 21 -total(dealer)<21 - total(player1):
    print(f"\nYou have{player1} for a total of {total(player1)} and the dealer has{dealer} for a total of {total(dealer)}")
    print("Dealer wins")
elif 21 - total(dealer)>21 - total(player1):
    print(f"\nYou have{player1} for a total of {total(player1)} and the dealer has{dealer} for a total of {total(dealer)}")
    print("You win")
