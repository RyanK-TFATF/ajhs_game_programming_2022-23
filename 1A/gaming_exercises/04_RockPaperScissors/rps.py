# 04_RockPaperScissors, Ryan Kelley, v0.1a
import random 

# Declare Variables 
p1Choice = ""
cpuChoice = ""
p1Score = 0
cpuScore = 0 

choices = [
    "rock",
    "paper",
    "scissors"
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

def cpuChoice(): 
    return choices[random.randint(0, 2)]

#print(cpuChoice())

def playerChoice():
    print("Ok, it's time to play Rock, Paper Scissors!")
    choice = input("Choose one and type rock, paper, or scissors.")
    print(f"You have selected {choice}.")
    while True: 
        correct = input("Is that correct? y / n\n")
        if correct == "y":
            break
        else: 
            choice = input("Choose one and type rock, paper, or scissors.\n")
    return choice 

#playerChoice() 

def determineWinner(p1Choice, cpuChoice):
    print(f"You have chosen {p1Choice}.  The CPU chose {cpuChoice}.")
    if p1Choice == "rock" and cpuChoice == "paper":
        print(f"Paper beats rock, so you have lost!\n")
        cpuScore += 1
    elif p1Choice == "rock" and cpuChoice == "scissors":        
        print(f"Rock beats scissors, so you have won!\n")
        p1Score += 1
    elif p1Choice == "rock" and cpuChoice == "rock":        
        print(f"This is a draw!\n")
    if p1Choice == "paper" and cpuChoice == "paper":
        print(f"This is a draw!\n")        
    elif p1Choice == "paper" and cpuChoice == "scissors":        
        print(f"Scissors beats paper, so you have lost!\n")
        cpuScore += 1
    elif p1Choice == "paper" and cpuChoice == "rock":        
        print(f"Paper beats rock, so you have won!\n")
        p1Score += 1
    if p1Choice == "scissors" and cpuChoice == "paper":
        print(f"Scissors beats paper, so you have won!\n")        
        p1Choice += 1
    elif p1Choice == "scissors" and cpuChoice == "scissors":        
        print(f"This is a draw!\n")          
    elif p1Choice == "scissors" and cpuChoice == "rock":        
        print(f"Rock beats scissors, so you have lost!\n")
        cpuScore += 1
    else:
        print("Something terrible has happened!  Please restart.\n")
        exit()
    return p1Score, cpuScore
        
    
cpuChoice = cpuChoice()
p1Choice = playerChoice()
determineWinner(p1Choice, cpuChoice)