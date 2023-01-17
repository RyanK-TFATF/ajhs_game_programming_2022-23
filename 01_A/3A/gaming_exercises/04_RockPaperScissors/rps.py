# 04_RockPaperScissors, Ryan Kelley, v0.
import random 

# Declare Variables 
playerChoice = ""
p1Score = 0

cpuChoice = ""
cpuScore = 0 

draws = 0 

choices = [
    "Rock", 
    "Paper", 
    "Scissors"
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

#cpuChoice = cpuRPS()

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

def determineRoundWinner(playerChoice, cpuChoice):
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

def calcScore(winner): 
    if winner == "player":
        p1Score = 1
        return p1Score
    elif winner == "cpu":
        cpuScore = 1
        return cpuScore
    elif winner == "draw":
        draws = 1
        return draws
    else:
        print("Unable to determine winner.  Please restart game.\n")
        exit()

def playGame(p1Score, cpuScore, draws):
    x = 0 
    while x < 100000: 
        cpuChoice = cpuRPS()
        p1Choice = cpuRPS()
        roundWin = determineRoundWinner(p1Choice, cpuChoice)
        if roundWin == "player":
            p1Score += calcScore(roundWin)
        if roundWin == "cpu":
            cpuScore += calcScore(roundWin)
        if roundWin == "draw":
            draws += calcScore(roundWin)
        print(f"Player Score: {p1Score}\n")
        print(f"CPU Score: {cpuScore}\n")
        print(f"Draws: {draws}\n")
        x += 1

playGame(p1Score, cpuScore, draws)
