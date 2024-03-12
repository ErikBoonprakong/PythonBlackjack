import random

deck = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 
        'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 
        'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 
        'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']
dealerHand = []
playerHand = []
dealerTotal = 0
playerTotal = 0
dealerHasBlackjack = False
playerHasBlackjack = False

def play():
    draw('player')
    draw('player')
    draw('dealer')
    draw('dealer')
    print(f"You have: {', '.join(playerHand)}")
    print(f"Your total: {playerTotal}")
    print(f"Dealer's hand: {', '.join(dealerHand)}")
    print(f"Dealer's total: {dealerTotal}")
    hitOrStickAction = input('Would you like to hit or stick? (h/s) \n')
    endTheGame = hitOrStick(hitOrStickAction)
    while (endTheGame == False):
        hitOrStickAction = input('Would you like to hit or stick? (h/s) \n')
        endTheGame = hitOrStick(hitOrStickAction)

def hasBlackjack(hand, who):
    global dealerHasBlackjack
    global playerHasBlackjack
    cardValueOne = hand[0][:-1]
    cardValueTwo = hand[1][:-1] 
    pictureCards = ['J', 'Q', 'K']
    if ((cardValueOne =='A' and cardValueTwo in pictureCards) or 
        (cardValueOne in pictureCards and cardValueTwo == 'A')):
        if (who == 'player'):
            print("You have blackjack!")
            playerHasBlackjack = True
        if (who == 'dealer'):
            print("The dealer has blackjack!")
            dealerHasBlackjack = True

def hitOrStick(action):
    print("\n")
    if (action.lower() == 's' or action.lower() == 'stick'):
        if (playerTotal < 17):
            print("You can't stick on less than 17!")
            return False
        else:
            if (len(playerHand) == 2):
                hasBlackjack(playerHand, 'player')
            if (len(dealerHand) == 2):
                hasBlackjack(dealerHand, 'dealer')
            while (dealerTotal < 17):
                hitDealer()
            if (dealerTotal <= 21):
                endGame('tbd')
        return True
    elif (action.lower() == 'h' or action.lower() == 'hit'):
        draw('player')
        print(f"You have: {', '.join(playerHand)}")
        print(f"Your total: {playerTotal}")
        if (playerTotal > 21):
            print("You went bust!")
            endGame('player')
            return True
        if (dealerTotal < 17):
            return hitDealer()
        print(f"Dealer's hand: {', '.join(dealerHand)}")
        print(f"Dealer's total: {dealerTotal}")
        return False
    else:
        print("Invalid input!")
        return False

def draw(hand):
    card = deck[random.randrange(len(deck))]
    if (hand == 'player'):
        playerHand.append(card)
        updateTotal('player', card)
    elif (hand == 'dealer'):
        dealerHand.append(card)
        updateTotal('dealer', card)
    deck.remove(card)

def updateTotal(hand, card):
    global playerTotal
    global dealerTotal
    cardValue = card[:-1]
    match cardValue:
        case 'A':
            cardValue = 11
        case 'J' | 'Q' | 'K':
            cardValue = 10
        case _:
            cardValue = int(cardValue)
    if (hand == 'player'):
        playerTotal += cardValue
    elif (hand == 'dealer'):
        dealerTotal += cardValue

def hitDealer():
    draw('dealer')
    print(f"Dealer's hand: {', '.join(dealerHand)}")
    print(f"Dealer's total: {dealerTotal}")
    if (dealerTotal > 21):
        print("The dealer went bust!")
        endGame('dealer')
        return True
    return False

def endGame(loser):
    global deck
    global dealerHand
    global playerHand
    global dealerHasBlackjack
    global playerHasBlackjack
    global dealerTotal
    global playerTotal
    winMsg = "You win! Yay!"
    loseMsg = "You lose! You absolutely suck!"
    drawMsg = "It's a draw!"
    if (loser == 'player'):
        print(loseMsg)
    if (loser == 'dealer'):
        print(winMsg)
    if (playerTotal <= 21 and dealerTotal <= 21):
        if (playerTotal > dealerTotal):
            print(winMsg)
        elif (dealerTotal > playerTotal):
            print(loseMsg)
        elif (dealerHasBlackjack == True and playerHasBlackjack == False):
            print(loseMsg)
        elif (playerHasBlackjack == True and dealerHasBlackjack == False):
            print(winMsg)
        elif (len(playerHand) > len(dealerHand)):
            print("You have more cards than the dealer!")
            print(winMsg)
        elif (len(dealerHand) > len(playerHand)):
            print("The dealer has more cards than you!")
            print(loseMsg)
        else:
            print(drawMsg)
    playAgain = input("Would you like to play again? (y/n)")
    if (playAgain.lower() == 'y' or playAgain.lower() == 'yes'):
        dealerHand = []
        playerHand = []
        deck = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 
                'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 
                'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 
                'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']
        dealerTotal = 0
        playerTotal = 0
        dealerHasBlackjack = False
        playerHasBlackjack = False
        print("\033[H\033[J", end="")
        play()

play()