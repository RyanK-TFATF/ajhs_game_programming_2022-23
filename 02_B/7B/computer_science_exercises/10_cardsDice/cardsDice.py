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

rollDice(1, 6)
rollDice(2, 20)
rollDice(4, 10)
rollDice(1, 100)
rollDice(10, 1000)
rollDice(1, 4)
rollDice(8, 8)

