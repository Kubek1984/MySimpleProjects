import sys, os, random



def shuffle():
    num = '2 3 4 5 6 7 8 9 10 J Q K A'
    colors = 'Hearts Diamonds Clubs Spades'
    deck = []
    numList = num.split(' ')
    colorsList = colors.split(' ')
    for i in numList:
        for j in colorsList:
            deck.append(i + ' ' + j)
    shuffleList = []
    while len(deck) != 0:
        
        rnd = random.randint(0, len(deck)-1)        
        card = deck[rnd]
        shuffleList.append(card[0])
        deck.pop(rnd)
        
    return shuffleList

def drawCardIndex(lenList):
    cardIndex = random.randint(0, lenList - 1)
    return cardIndex

def cardValue(card, result):
    if card.isdigit():
        value = int(card)
    elif card.lower() == 'j' or card.lower() == 'q' or card.lower() == 'k':
        value = 10
    elif card.lower() == 'a':
        value = cardValueAce(result)

    return value

def cardValueAce(result):
    if result + 11 <= 21:
        value = 11    
    else:
        value = 1
    return value

def compare(plResult, cmResult):
    
    os.system('clear')
    if plResult < 22 and plResult > cmResult:
        print('\nPlayer Cards : ', end = ' ')
        for i in playerCards:
            print(f'[{i}]', end = ' ')
        print(f'Result: {playerResult}', end ='')
        print('\t\tComputer Cards : ', end = ' ')            
        for i in computerCards:
            print(f'[{i}]', end = ' ')
        print(f'Result: {computerResult}\n')
        print('\t\t\t\tYOU WIN!!!\n\n')

    elif plResult == cmResult :
        print('\nPlayer Cards : ', end = ' ')
        for i in playerCards:
            print(f'[{i}]', end = ' ')
        print(f'Result: {playerResult}', end ='')
        print('\t\tComputer Cards : ', end = ' ')            
        for i in computerCards:
            print(f'[{i}]', end = ' ')
        print(f'Result: {computerResult}\n')
        print('\t\t\t\tDRAW!!!\n\n')
    elif cmResult < 22 and cmResult > plResult:
        print('\nPlayer Cards : ', end = ' ')
        for i in playerCards:
            print(f'[{i}]', end = ' ')
        print(f'Result: {playerResult}', end ='')
        print('\t\tComputer Cards : ', end = ' ')            
        for i in computerCards:
            print(f'[{i}]', end = ' ')
        print(f'Result: {computerResult}\n')
        print('\t\t\t\tYOU LOOSE!!!\n\n')
    



def game():
    global playerCards, playerResult, computerCards, computerResult
    while True:
        deck = shuffle()
        
        while len(deck) >= 9 :
            playerCards =[]
            playerResult = 0
            for i in range(2):
                index = drawCardIndex(len(deck))
                card = deck[index]
                cardInt = cardValue(card, playerResult)
                playerResult += cardInt
                playerCards.append(card)
                deck.pop(index)
                
            computerCards = []
            computerResult = 0
            for i in range(2):
                index = drawCardIndex(len(deck))
                card = deck[index]
                cardInt = cardValue(card, computerResult)
                computerResult += cardInt
                computerCards.append(card)
                deck.pop(index)
            
            print('\nPlayer Cards : ', end = ' ')
            for i in playerCards:
                print(f'[{i}]', end = ' ')
            print(f'Result: {playerResult}', end ='')
            print('\t\tComputer Cards : ', end = ' ')            
            print(f'[{computerCards[0]}] [ ]\n')

            blackjack = 0
            while True:
                
                if blackjack == 1:
                    compare(playerResult, computerResult)
                    break
                print(f'Deck: {len(deck)}')
                print('''
                
                    1. Quit Program - "Enter"
                    2. Hit - "H"
                    3. Stand - "S"
                    ''')
                ask = input('Hit or Stand? H/S : ')
                
                if ask.lower() == 'h':
                    index = drawCardIndex(len(deck))
                    card = deck[index]
                    cardInt = cardValue(card, playerResult)
                    playerResult += cardInt
                    playerCards.append(card)
                    deck.pop(index)
                    
                    if playerResult > 21 :
                        os.system('clear')
                        print('\nPlayer Cards : ', end = ' ')
                        for i in playerCards:
                            print(f'[{i}]', end = ' ')
                        print(f'Result: {playerResult}\t\tBUSTED. You Lose!!!', end =' ')
                        print('\t\tComputer Cards : ', end = ' ')
                        for i in computerCards:
                            print(f'[{i}]', end = ' ')
                        print(f'Result: {computerResult}\n')
                        print()
                        break 

                    elif playerResult == 21:
                        os.system('clear')
                        print('\nPlayer Cards : ', end = ' ')
                        for i in playerCards:
                            print(f'[{i}]', end = ' ')
                        print(f'Result: {playerResult}\t\tBLACK JACK\t', end = ' ')
                        print('\t\tComputer Cards : ', end = ' ')
                        print(f'[{computerCards[0]}] [ ]\n')
                        blackjack += 1
                    else:
                        os.system('clear')
                        print('\nPlayer Cards : ', end = ' ')
                        for i in playerCards:
                            print(f'[{i}]', end = ' ')
                        print(f'Result: {playerResult}', end = ' ')
                        print('\t\tComputer Cards : ', end = ' ')
                        print(f'[{computerCards[0]}] [ ]\n')
                elif ask.lower() == 's':
                    if computerResult < 16 :
                        while computerResult < 16:
                            index = drawCardIndex(len(deck))
                            card = deck[index]
                            cardInt = cardValue(card, computerResult)
                            computerResult += cardInt
                            computerCards.append(card)
                            deck.pop(index)
                        compare(playerResult, computerResult)
                        break
                    else:
                        compare(playerResult, computerResult)
                        break
                else:
                    sys.exit()
                     
                    





game()