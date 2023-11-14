# Example Game Functions, Ryan Kelley, v0.0 
import random 

# VARIABLE DELCARATIONS 
batterSkill = 0 # Scale of 0 - 100, 100 being best. 
pitchTypes = ["fastball", 
             "curveball", 
             "slider"]
batterPosition = None # Low, Middle, High are the options. 
pitchPosition = None # Low, Middle, High are the options. 

def playerBatting(batterSkill, pitchType, batterPosition, pitchPosition):
    if batterSkill > 90 and pitchType == "fastball" and pitchPosition == "high" and batterPosition == "high":
        swingScore = random.randint(0, 100)
        if swingScore > 10: 
            print("The batter swings and....HITS!\n")
        else:
            print("It's a swing and a miss!\n")
    elif batterSkill > 80 and pitchType == "fastball" and pitchPosition == "high" and batterPosition == "low":
        swingScore = random.randint(0, 100)
        if swingScore > 50: 
            print("The batter swings and....HITS!\n")
        else:
            print("It's a swing and a miss!\n")
    else:
        print("It's a swing and a miss!\n")

playerBatting(95, "fastball", "high", "high")
playerBatting(35, "fastball", "high")

def coinFlip():
    coinFlip = random.randint(1, 2)
    if coinFlip == 1:
        coinFlip = "Heads"
    elif coinFlip == 2:
        coinFlip = "Tails"
    else:
        coinFlip = None # Error has occured
    return coinFlip 


def functionThree():
    pass

def functionFour(): 
    pass