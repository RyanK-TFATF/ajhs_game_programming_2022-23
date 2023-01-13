# 04_RockPaperScissors, Ryan Kelley, v0.2
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

# Game Functions 
def displayInstructions(): 
    print("*==========================================*")
    print("*                Welcome to                *")
    print("*    Ryan's Rock -- Paper -- Scissors      *")
    print("*                                          *")
    print("* To play, you will choose Rock, Paper, or *")
    print("* Scissors.                                *")
    print("*                                          *")
    print("* Rules:                                   *")
    print("* Rock Beats Scissors                      *")
    print("* Paper Beats Rock                         *")
    print("* Scissors Beats Paper                     *")
    print("*                                          *")
    print("* Winner of each round gets 1 point.       *")
    print("* First to score 3 points wins the match!  *")
    print("*==========================================*")

#displayInstructions()

# Make CPU Selection 
def cpuChoice(): 
    return choices[random.randint(0, 2)]

cpuChoice = cpuChoice()

# Player Choice 
def playerChoice(): 
    print("Ok, let's get down to business and play rock, paper, scissors!")
    playerChoice = input("Please type Rock, Paper, or Scissors and press [ENTER].\n")
    print(f"You have chosen {playerChoice}.\n")
    while True: 
        isCorrect = input("Is this correct? Yes / No\n")
        if isCorrect == "Yes":
            break
        else: 
            playerChoice = input("Please type Rock, Paper, or Scissors and press [ENTER].\n")
    return playerChoice

#playerChoice = cpuChoice()

def roundWinner(playerChoice, cpuChoice):
    print(f"You have chosen {playerChoice}.\n")
    print(f"The CPU has chosen {cpuChoice}.\n")
    if playerChoice == "Rock" and cpuChoice == "Rock": 
        print("That is a draw.  Womp womp.\n")
    elif playerChoice == "Rock" and cpuChoice == "Paper": 
        print("The CPU wins, you scrub.\n")
    elif playerChoice == "Rock" and cpuChoice == "Scissors": 
        print("You win! Much wow.\n")
    elif playerChoice == "Paper" and cpuChoice == "Rock": 
        print("You win! Much wow.\n")
    elif playerChoice == "Paper" and cpuChoice == "Paper": 
        print("That is a draw.  Womp womp.\n")
    elif playerChoice == "Paper" and cpuChoice == "Scissors": 
        print("The CPU wins, you scrub.\n")
    elif playerChoice == "Scissors" and cpuChoice == "Rock": 
        print("The CPU wins, you scrub.\n")
    elif playerChoice == "Scissors" and cpuChoice == "Paper": 
        print("You win! Much wow.\n")
    elif playerChoice == "Scissors" and cpuChoice == "Scissors": 
        print("That is a draw.  Womp womp.\n")
    else:
        print("Unable to determine a winner.  Please restart.") 
        exit()

x = 0 
while x <= 500: 
   playerChoice = cpuChoice()
   cpuChoice = cpuChoice()
   roundWinner(playerChoice, cpuChoice)
   x += 1


