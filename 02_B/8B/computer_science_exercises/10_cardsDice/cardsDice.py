# Cards & Dice, Ryan Kelley, 05/03/23 
#import random # BRING THE ENTIRE TOOL BOX 
from random import randint # BRING JUST THE TOOL NEEDED
def shuffleDeck(numShuffle):    
    pass

def startTimer(numSeconds):
    pass

def drawCard(numCards):
    pass

def getValue(card): 
    pass
    return value 

def rollDice(numDice, sizeDice):
    sum = 0
    numRolls = 0 
    while numRolls < numDice:
        sum += randint(1, sizeDice)
        numRolls += 1
    print(sum)
    return sum 

def main(): 
    currentScore = 0 
    shuffleDeck(5)
    drawCard(5)
    yourHand = []
    for eachCard in yourHand: 
        value = getValue(card)
        if value >= 2 or value <= 10:
            currentScore += value 
        elif value == 11: # Jack
            currentScore += rollDice(1, 6)
        elif value == 12: # Queen
            currentScore += rollDice(1, 8)
        elif value == 13: # King 
            currentScore += rollDice(1, 10)
        elif value == 14: # Ace
            currentScore += rollDice(1, 12)
        else: # UNIDENTIFIED CARD
            print("Error, unknown card.\n")
            currentScore = 0
    
    startTimer(120)

    while sandInTimer == True: # One grain of sand up top means run the loop!
        drawCard(1)
        value = getValue(card)
        if value >= 2 or value <= 10:
            currentScore -= value 
        elif value == 11: # Jack
            currentScore -= rollDice(1, 6)
        elif value == 12: # Queen
            currentScore -= rollDice(1, 8)
        elif value == 13: # King 
            currentScore -= rollDice(1, 10)
        elif value == 14: # Ace
            currentScore -= rollDice(1, 12)
        else: # UNIDENTIFIED CARD
            print("Error, unknown card.\n")
            currentScore = 0

    if currentScore % 2 == 0:
        getCandy(10, 10)
    else: 
        getCandy(20)

