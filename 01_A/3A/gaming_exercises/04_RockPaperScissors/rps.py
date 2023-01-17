# 04_RockPaperScissors, Ryan Kelley, v0.5a
import random 

# Declare Variables 
playerChoice = ""
playerScore = 0

cpuChoice = ""
cpuScore = 0 

draws = 0 

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
def cpuRPS(): 
    return choices[random.randint(0, 2)]

cpuChoice = cpuRPS()

# Player Choice 
def playerRPS(): 
    print("Ok, let's get down to business and play rock, paper, scissors!")
    playerChoice = input("Please type Rock, Paper, or Scissors and press [ENTER].\n")
    playerChoice = playerChoice[0].lower()    
    if playerChoice == "r":
        playerChoice = "Rock"
    elif playerChoice == "s":
        playerChoice = "Scissors"
    elif playerChoice == "p":
        playerChoice = "Paper"
    else:
        print("Error Choosing Rock, Paper, Scissors.")
    print(f"You have chosen {playerChoice}.\n")

    while True: 
        isCorrect = input("Is this correct? Yes / No\n")
        isCorrect = isCorrect[0].lower()
        if isCorrect == "y":
            break
        else: 
            playerChoice = input("Please type Rock, Paper, or Scissors and press [ENTER].\n")
            if playerChoice == "r":
                playerChoice = "Rock"
            elif playerChoice == "s":
                playerChoice = "Scissors"
            elif playerChoice == "p":
                playerChoice = "Paper"
            else:
                print("Error Choosing Rock, Paper, Scissors.")
    return playerChoice

#playerRPS()

def roundWinner(playerChoice, cpuChoice):
    print(f"You have chosen {playerChoice}.\n")
    print(f"The CPU has chosen {cpuChoice}.\n")
    if playerChoice == "Rock" and cpuChoice == "Rock": 
        print("That is a draw.  Womp womp.\n")
        roundWinner = "draw"
    elif playerChoice == "Rock" and cpuChoice == "Paper": 
        print("The CPU wins, you scrub.\n")
        roundWinner = "cpu"
    elif playerChoice == "Rock" and cpuChoice == "Scissors": 
        print("You win! Much wow.\n")        
        roundWinner = "player"
    elif playerChoice == "Paper" and cpuChoice == "Rock": 
        print("You win! Much wow.\n")
        roundWinner = "player"
    elif playerChoice == "Paper" and cpuChoice == "Paper": 
        print("That is a draw.  Womp womp.\n")
        roundWinner = "draw"
    elif playerChoice == "Paper" and cpuChoice == "Scissors": 
        print("The CPU wins, you scrub.\n")
        roundWinner = "cpu"
    elif playerChoice == "Scissors" and cpuChoice == "Rock": 
        print("The CPU wins, you scrub.\n")
        roundWinner = "cpu"
    elif playerChoice == "Scissors" and cpuChoice == "Paper": 
        print("You win! Much wow.\n")
        roundWinner = "player"
    elif playerChoice == "Scissors" and cpuChoice == "Scissors": 
        print("That is a draw.  Womp womp.\n")
        roundWinner = "draw"
    else:
        print("Unable to determine a winner.  Please restart.") 
        exit()
    return roundWinner 