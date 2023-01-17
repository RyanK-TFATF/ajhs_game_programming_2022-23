# 04_RockPaperScissors, Ryan Kelley, v0.1a
import random 

# Declare Variables 
p1Choice = ""
cpuChoice = ""
p1Score = 0
cpuScore = 0 

choices = [
    "r",
    "p",
    "s"
]

# Define Functions 
def displayInstructions(): 
    print("+**************************************************+")
    print("+ Welcome to Ryan's Rock-Paper-Scissors Simulator! +")
    print("+ For this game, you will choose Rock, Paper, or   +")
    print("+ Scicssors!                                       +")
    print("+ The rules of this game are:                      +")
    print("+ Rock Beats Scissors                              +")
    print("+ Scissors Beats Paper                             +")
    print("+ Paper Beats Rock                                 +")
    print("+                                                  +")
    print("+                                                  +")
    print("+ If you win, you will score 1 point.              +")
    print("+ The first player to score 3 points will win!     +")
    print("+**************************************************+")

# displayInstructions()

def cpuRPS(): 
    return choices[random.randint(0, 2)]

#print(cpuChoice())

def playerRPS():
    print("Ok, it's time to play Rock, Paper Scissors!")
    choice = input("Choose one and type rock, paper, or scissors.")
    print(f"You have selected {choice}.")
    while True: 
        correct = input("Is that correct? Yes / No\n")
        correct = correct[0].lower()        
        if correct == "y":
            break
        else: 
            choice = input("Choose one and type rock, paper, or scissors.\n")
    choice = choice[0].lower()    
    return choice 

#print(playerRPS()) 

def determineWinner(p1Choice, cpuChoice):
    print(f"You have chosen {p1Choice}.  The CPU chose {cpuChoice}.")
    if p1Choice == "r" and cpuChoice == "p":
        print(f"Paper beats rock, so you have lost!\n")
        winner = "cpu"
    elif p1Choice == "r" and cpuChoice == "s":        
        print(f"Rock beats scissors, so you have won!\n")
        winner = "player"
    elif p1Choice == "r" and cpuChoice == "r":        
        print(f"This is a draw!\n")
        winner = "draw"
    elif p1Choice == "p" and cpuChoice == "p":
        print(f"This is a draw!\n")        
        winner = "draw"
    elif p1Choice == "p" and cpuChoice == "s":        
        print(f"Scissors beats paper, so you have lost!\n")
        winner = "cpu"
    elif p1Choice == "p" and cpuChoice == "r":        
        print(f"Paper beats rock, so you have won!\n")
        winner = "player"
    elif p1Choice == "s" and cpuChoice == "p":
        print(f"Scissors beats paper, so you have won!\n")        
        winner = "winner"
    elif p1Choice == "s" and cpuChoice == "s":        
        print(f"This is a draw!\n")          
        winner = "draw"
    elif p1Choice == "s" and cpuChoice == "r":        
        print(f"Rock beats scissors, so you have lost!\n")
        winner = "cpu"
    else:
        print("Something terrible has happened!  Please restart.\n")
        exit()
    return winner 
        
x = 0 
while x < 100:    
    cpuChoice = cpuRPS()
    p1Choice = cpuRPS()
    determineWinner(p1Choice, cpuChoice)
    x += 1 