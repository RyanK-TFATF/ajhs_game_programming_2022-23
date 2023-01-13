# Rock Paper Scissors -- Ryan Kelley -- v0.1a
import random 

# Declare Variables 
playerChoice = ""
playerScore = 0 

cpuChoice = ""
cpuScore = 0 

choices = [
    "rock",
    "paper",
    "scissors"
]

# Function Declarations 
def displayMenu(): 
    print("/************************************************\\")
    print("|               Welcome to the                   |")
    print("|  World's Toughest Rock-Paper-Scissors Robot    |")
    print("|                                                |")
    print("|                Written By                      |")
    print("|             Ryan Kelley, 7B                    |")
    print("|                                                |")
    print("| You will select Rock, Paper, or Scissors.      |")
    print("| The CPU will do the same.                      |")
    print("|                                                |")
    print("| Using these rules, a winner is determined:     |")
    print("| ROCK beats SCISSORS                            |")
    print("| PAPER beats ROCK                               |")
    print("| SCISSORS beats PAPER                           |")
    print("|                                                |")
    print("| Each round is worth 1 point.                   |")
    print("| First player to 3 points wins the match.       |")
    print("|                                                |")
    print("\\************************************************/")

# displayMenu()

# CPU Choice 
def cpuRPS(): 
    return choices[random.randint(0, 2)]

# print(cpuRPS())

# Player Choice 
def playerRPS():
    print("Please choose your option for this round!\n")
    choice = input("Please type Rock, Paper, or Scissors and press ENTER.\n")
    print(f"You have selected {choice}.\n")
    while True: 
        correct = input("Is that correct? Yes or No, then ENTER.\n")
        if correct == "Yes":
            break 
        else: 
            choice = input("Please type Rock, Paper, or Scissors and press ENTER.\n")
    return choice 

# playerRPS()

def determineWinner(playerChoice, cpuChoice):
    print(f"You have selected {playerChoice}.\n")
    print(f"The CPU has selected {cpuChoice}.\n")
    if playerChoice == "Rock" and cpuChoice == "Rock": 
        print("That is a draw!\n")
    elif playerChoice == "Rock" and cpuChoice == "Paper": 
        print("The CPU wins!\n")
    elif playerChoice == "Rock" and cpuChoice == "Scissors": 
        print("You win!\n")
    # Use elif statements to determine the winner if the player chose Paper, and then Scissors. 
    
    else: 
        print("Unable to determine a winner.  Please restart the game!\n")
        exit()

    
    
    
    




