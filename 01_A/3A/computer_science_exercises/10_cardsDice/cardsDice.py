#import random # THIS BRINGS THE WHOLE TOOL BOX. 
from random import randint # BRING JUST THE TOOL NEEDED

def shuffleDeck(numShuffles):
    pass # Tells Python our code is not finished, but give no error.

def startTimer(numSeconds): 
    pass

def drawCard(numCards):
    pass

def getValue(card):
    value = 0 
    pass
    return value 

def rollDice(numDice, sizeDice):
    sum = 0
    numRolls = 0 
    while numRolls < numDice:
        sum += randint(1, sizeDice)
        numRolls += 1
    print(f"You rolled {numDice}d{sizeDice} and got a sum of {sum}.")
    return sum 

def main():
    currentScore = 0 
    shuffleDeck(5)
    drawCard(5)
    for eachCard in yourHand: 
        value = getValue(card)
        if value <= 10: 
            currentScore += value 
        elif value == 11: # Jack 
            currentScore += rollDice(1, 6)
        elif value == 12: # Queen 
            currentScore += rollDice(1, 8)
        elif value == 13: # King
            currentScore += rollDice(1, 10)
        elif value == 14: # Ace 
            currentScore += rollDice(1, 12)
        else: 
            currentScore = 0
            print("Error!")

    startTimer(120)

    while timeRemaining == True: # If sand up top, keep going!
        drawCard(1)
        value = getValue(card)
        if value <= 10: 
            currentScore -= value 
        elif value == 11: # Jack 
            currentScore -= rollDice(1, 6)
        elif value == 12: # Queen 
            currentScore -= rollDice(1, 8)
        elif value == 13: # King
            currentScore -= rollDice(1, 10)
        elif value == 14: # Ace 
            currentScore -= rollDice(1, 12)
        else: 
            currentScore = 0
            print("Error!")

    if currentValue % 2 == 0:
        getCandy(10, 10)
    else: 
        getCandy(20)