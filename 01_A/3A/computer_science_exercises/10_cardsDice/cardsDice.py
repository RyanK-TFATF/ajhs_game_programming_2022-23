#import random # THIS BRINGS THE WHOLE TOOL BOX. 
from random import randint # BRING JUST THE TOOL NEEDED

def shuffleDeck(numShuffles):
    pass # Tells Python our code is not finished, but give no error.

# CALL THE FUNCTION 
shuffleDeck(7)
shuffleDeck(500)

def startTimer(numSeconds): 
    pass

startTimer(120)

def drawCard(numCards):
    pass

def getValue(card):
    value = 0 
    pass
    return value 

getValue('Jack')

def rollDice(numDice, sizeDice):
    sum = 0
    numRolls = 0 
    while numRolls < numDice:
        sum += randint(1, sizeDice)
        numRolls += 1
    print(f"You rolled {numDice}d{sizeDice} and got a sum of {sum}.")
    return sum 



