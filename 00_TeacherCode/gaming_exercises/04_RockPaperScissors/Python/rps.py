# 04_RockPaperScissors, Ryan Kelley, v2.0a
import random 

# Declare Variables 
p1Choice = ""
cpuChoice = ""
p1Score = 0
cpuScore = 0 
draws = 0

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

def cpuRPS(): 
    return choices[random.randint(0, 2)]

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
    return choice 

def determineRoundWinner(p1Choice, cpuChoice):
    print(f"You have chosen {p1Choice}.  The CPU chose {cpuChoice}.")
    if p1Choice == "rock" and cpuChoice == "paper":
        print(f"Paper beats rock, so you have lost!\n")
        roundWinner = "cpu"
    elif p1Choice == "rock" and cpuChoice == "scissors":        
        print(f"Rock beats scissors, so you have won!\n")
        roundWinner = "player"
    elif p1Choice == "rock" and cpuChoice == "rock":        
        print(f"This is a draw!\n")
        roundWinner = "draw"
    elif p1Choice == "paper" and cpuChoice == "paper":
        print(f"This is a draw!\n")        
        roundWinner = "draw"
    elif p1Choice == "paper" and cpuChoice == "scissors":        
        print(f"Scissors beats paper, so you have lost!\n")
        roundWinner = "cpu"
    elif p1Choice == "paper" and cpuChoice == "rock":        
        print(f"Paper beats rock, so you have won!\n")
        roundWinner = "player"
    elif p1Choice == "scissors" and cpuChoice == "paper":
        print(f"Scissors beats paper, so you have won!\n")        
        roundWinner = "player"
    elif p1Choice == "scissors" and cpuChoice == "scissors":        
        print(f"This is a draw!\n")          
        roundWinner = "draw"
    elif p1Choice == "scissors" and cpuChoice == "rock":        
        print(f"Rock beats scissors, so you have lost!\n")
        roundWinner = "cpu"
    else:
        print("Something terrible has happened!  Please restart.\n")
        exit()
    return roundWinner 
        
def calcScore(roundWinner):
    if roundWinner == "player":   
        p1Score = 1     
        return p1Score 
    elif roundWinner == "cpu":        
        cpuScore = 1
        return cpuScore
    else: 
        draws = 1 
        return draws 

def matchWinner(p1Score, cpuScore):
    if p1Score >= 5:
        print("Congratulations, you have won the match!")
        return True        
    elif cpuScore >= 5:
        print("Unfortunately, you have lost to the CPU.\n")        
        return True
    else:
        return False

def playGame(p1Score, cpuScore, draws):    
    while True:    
        cpuChoice = cpuRPS()
        p1Choice = playerRPS()
        roundWinner = determineRoundWinner(p1Choice, cpuChoice)
        if roundWinner == "player":
            p1Score += calcScore(roundWinner) #, p1Score, cpuScore, draws)    
        if roundWinner == "cpu":
            cpuScore += calcScore(roundWinner) #, p1Score, cpuScore, draws)
        if roundWinner == "draw":
            draws += calcScore(roundWinner) #, p1Score, cpuScore, draws)
    
        print(f"Player 1 Score: {p1Score}\n")
        print(f"CPU Score: {cpuScore}\n")
        print(f"Draws: {draws}\n")

        if matchWinner(p1Score, cpuScore) == True:            
            break
      
playGame(p1Score, cpuScore, draws)