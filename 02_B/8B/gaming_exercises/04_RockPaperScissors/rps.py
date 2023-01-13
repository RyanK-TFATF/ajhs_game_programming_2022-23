# Rock Paper Scissors, Ryan Kelley, v0.0 

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