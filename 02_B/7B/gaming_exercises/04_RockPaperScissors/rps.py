# Rock Paper Scissors -- Ryan Kelley -- v0.1a
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

def determineRoundWinner(playerChoice, cpuChoice):
    print(f"You have selected {playerChoice}.\n")
    print(f"The CPU has selected {cpuChoice}.\n")
    if playerChoice == "Rock" and cpuChoice == "Rock": 
        print("That is a draw!\n")
        winner = "draw"
    elif playerChoice == "Rock" and cpuChoice == "Paper": 
        print("The CPU wins!\n")
        winner = "cpu"
    elif playerChoice == "Rock" and cpuChoice == "Scissors": 
        print("You win!\n")
        winner = "player"
    elif playerChoice == "Paper" and cpuChoice == "Rock": 
        print("You win!\n")        
        winner = "player"
    elif playerChoice == "Paper" and cpuChoice == "Paper": 
        print("That is a draw!\n")        
        winner = "draw"
    elif playerChoice == "Paper" and cpuChoice == "Scissors": 
        print("The CPU wins!\n")
        winner = "cpu"
    elif playerChoice == "Scissors" and cpuChoice == "Rock": 
        print("The CPU wins!\n")
        winner = "cpu"
    elif playerChoice == "Scissors" and cpuChoice == "Paper": 
        print("You win!\n")        
        winner = "player"
    elif playerChoice == "Scissors" and cpuChoice == "Scissors":         
        print("That is a draw!\n")
        winner = "draw"
    else:
        print("Error Code 0512: Error in determineRoundWinner() Function")
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
    if playerScore == 5: 
        print("Congratulations, a winner is you!  You have defeated the CPU.")
        return True
    elif cpuScore == 5:
        print("What a scrub, you lost to the machine.")
        return True 
    else: 
        return False 

def playRPS(playerScore, cpuScore, draws):
    displayMenu()
    while True: 
        cpuChoice = cpuRPS()
        playerChoice = playerRPS()
        roundWin = determineRoundWinner(playerChoice, cpuChoice)
        if roundWin == "player":
            playerScore += calcScore(roundWin)
        elif roundWin == "cpu":
            cpuScore += calcScore(roundWin)
        elif roundWin == "draw":
            draws += calcScore(roundWin)
        else: 
            print("Error Code 1234 in playRPS()")
        
        print(f"Player Score: {playerScore}")
        print(f"CPU Score: {cpuScore}")
        print(f"Draws: {draws}")

        if determineMatchWinner(playerScore, cpuScore) == True:
            break 
        


    

    
    
    
    




