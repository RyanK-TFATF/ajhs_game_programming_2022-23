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

# x = 0 
# while x <= 50: 
#     print(cpuChoice())
#     x += 1


