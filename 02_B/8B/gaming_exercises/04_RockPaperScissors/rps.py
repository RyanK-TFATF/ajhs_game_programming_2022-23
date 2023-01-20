# Rock Paper Scissors, Ryan Kelley, v0.0 
import random 

# Declare Variables 
playerChoice = ""
playerScore = 0

cpuChoice = ""
cpuScore = 0 

draws = 0 

choices = [
    "Rock",
    "Paper",
    "Scissors"
]

# Function Definitions 
def displayMenu(): 
    print("+==============================+")
    print("+      Welcome to              +")
    print("+ Rock-Paper-Scissors Robot500 +")
    print("+                              +")
    print("+     Brought to you by        +")
    print("+        Ryan K., 8B           +")
    print("+                              +")
    print("+                              +")
    print("+ You will chose one of these  +")
    print("+ options:                     +")
    print("+ Rock, Paper, or Scissors     +")
    print("+                              +")
    print("+ The CPU will do the same.    +")
    print("+                              +")
    print("+ Using these rules a winner   +")
    print("+ will be selected:            +")
    print("+                              +")
    print("+ ROCK beats SCISSORS          +")
    print("+ PAPER beats ROCK             +")
    print("+ SCISSORS beats PAPER         +")
    print("+                              +")
    print("+ Winner scores 1 point.       +")
    print("+ First player to score 3      +")
    print("+ points wins the match.       +")
    print("+==============================+")

#displayMenu()

# CPU Choice 
def cpuRPS(): 
    return choices[random.randint(0, 2)]

# x = 0 
# while x < 100:     
#     print(cpuRPS())
#     x += 1

def playerRPS(): 
    print("Let's get ready to RRRRRRRUUUUUUMMMMMBLE!\n")
    choice = input("Please choose Rock, Paper, or Scissors and push ENTER.\n")
    print(f"You have entered {choice}.\n")
    while True: 
        correct = input("Is that correct? Yes or No, then ENTER.\n")
        if correct == "Yes": 
            break 
        else: 
            choice = input("Please choose Rock, Paper, or Scissors and push ENTER.\n")
    return choice 

#playerRPS()

def determineRoundWinner(playerChoice, cpuChoice):
    print(f"You have chosen {playerChoice}.\n")
    print(f"The CPU has chosen {cpuChoice}.\n")
    if playerChoice == "Rock" and cpuChoice == "Rock": 
        print("It is a draw. Womp womp.\n")
        winner = "draw"
    elif playerChoice == "Rock" and cpuChoice == "Paper": 
        print("The CPU wins, scrub.\n")
        winner = "cpu"
    elif playerChoice == "Rock" and cpuChoice == "Scissors": 
        print("A winner is you!\n")
        winner = "player"
    elif playerChoice == "Paper" and cpuChoice == "Rock": 
        print("A winner is you!\n")
        winner = "player"
    elif playerChoice == "Paper" and cpuChoice == "Paper": 
        print("It is a draw. Womp womp.\n")        
        winner = "draw"
    elif playerChoice == "Paper" and cpuChoice == "Scissors": 
        print("The CPU wins, scrub.\n")
        winner = "cpu"
    elif playerChoice == "Scissors" and cpuChoice == "Rock": 
        print("The CPU wins, scrub.\n")
        winner = "cpu"
    elif playerChoice == "Scissors" and cpuChoice == "Paper": 
        print("A winner is you!\n")        
        winner = "player"
    elif playerChoice == "Scissors" and cpuChoice == "Scissors":        
        print("It is a draw. Womp womp.\n")        
        winner = "draw"
    else: 
        print("There is a fatal error and winner cannot be determined.\n")
        print("Your computer will now explode.  Good luck.\n")
        exit()
    return winner 

def calcScore(winner):
    if winner == "player": 
        playerScore = 1
        return playerScore 
    elif winner == "cpu":
        cpuScore = 1
        return cpuScore
    else: 
        draws = 1
        return draws

def determineMatchWinner(playerScore, cpuScore): 
    if playerScore == 50000: 
        print("Congrats!  You have beaten the CPU!\n")    
        return True 
    elif cpuScore == 50000:
        print("You scrub.  You lost to the CPU.\n")
        return True 
    else: 
        return False 

def playGame(playerScore, cpuScore, draws): 
    displayMenu()
    while True: 
        cpuChoice = cpuRPS()
        playerChoice = cpuRPS()
        roundWin = determineRoundWinner(playerChoice, cpuChoice)
        if roundWin == "player": 
            playerScore += calcScore(roundWin)
        if roundWin == "cpu": 
            cpuScore += calcScore(roundWin)
        if roundWin == "draw": 
            draws += calcScore(roundWin)
        
        print(f"Player Score: {playerScore}")
        print(f"CPU Score: {cpuScore}")
        print(f"Draws: {draws}")

        if determineMatchWinner(playerScore, cpuScore) == True: 
            break 
        
playGame(playerScore, cpuScore, draws)

        



    

    
    

    
