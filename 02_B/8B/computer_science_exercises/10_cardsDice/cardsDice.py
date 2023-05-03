# Cards & Dice, Ryan Kelley, 05/03/23 
#import random # BRING THE ENTIRE TOOL BOX 
from random import randint # BRING JUST THE TOOL NEEDED
def shuffleDeck(numShuffle):    
    pass

#shuffleDeck(3)

def startTimer(numSeconds):
    pass

minute = 60
startTimer(3 * minute)

def drawCard(numCards):
    pass

def getValue(card): 
    pass
    return value 

def rollDice(numDice, sizeDice):
    sum = 0
    numRolls = 0 
    while numRolls != numDice:
        sum += randint(1, sizeDice)
        numRolls += 1
    print(sum)
    return sum 

while True:
    sum = rollDice(4, 8)
    if sum == 4:
        break 

