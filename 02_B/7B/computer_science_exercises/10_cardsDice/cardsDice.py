# Ryan Kelley, Cards & Dice, 05/03/23 
#import random # BRING THE WHOLE TOOL BOX. 
from random import randint # BRING JUST THE SPECIFIC TOOL

def shuffleDeck(numShuffles):
    pass

def startTimer(time):
    # Time is measured in seconds. 
    pass

def drawCard(numCards):
    pass

def getValue(card):
    pass
    return value 

def rollDice(numDice, sizeDice):
    sum = 0
    diceRolls = 0
    while diceRolls < numDice:
        sum += randint(1, sizeDice)
        diceRolls += 1
    print(sum)
    return sum 

def main():
    currentScore = 0 
    shuffleDeck(7)
    drawCard(5)

    for eachCard in yourHand: 
        value = getValue(card)
        if value >= 2 or value <= 10: 
            currentScore += value 
        elif value == 11:  # Jack 
            currentScore += rollDice(1, 6)
        elif value == 12:  # Queen
            currentScore += rollDice(1, 8)
        elif value == 13:  # King
            currentScore += rollDice(1, 10)
        elif value == 14:  # Ace
            currentScore += rollDice(1, 12)
        else:
            print("Card not identified.")
            currentScore = 0
    startTimer(120)

    while timeRemaining > 0: # One itty bitty grain of sand up top means run the loop!
        drawCard(1)
        value = getValue(card)
        if value >= 2 or value <= 10: 
            currentScore -= value 
        elif value == 11:  # Jack 
            currentScore -= rollDice(1, 6)
        elif value == 12:  # Queen
            currentScore -= rollDice(1, 8)
        elif value == 13:  # King
            currentScore -= rollDice(1, 10)
        elif value == 14:  # Ace
            currentScore -= rollDice(1, 12)
        else:
            print("Card not identified.")
            currentScore = 0

    if currentScore % 2 == 0:
        getCandy(10, 10)
    else: 
        getCandy(20)

    




