# Pick the secret number from a range for the possible numbers (i.e. 0-10, 0-100, 100-200)
# Provide the player X number of guesses, based on range of numbers.  
# Player guesses the number. 
# Compare guess to secret number. 
# If the guess is correct what should happen?
    # Award the player a point. 
    # Print a 'win' message on the screen. 
# If the guess is incorrect, what should happen? 
    # Indicate if guess is high/low compared to secret number. 
# If the player does not guess correctly before hitting limit, what happens?
    # Award a point to the CPU. 
    # Print a loss message.  
# First player to score at least 3 points is declared the winner. 

# Guess a Number, Ryan Kelley, v0.0 
import random 

# DECLARATIONS 
secretNumber = -1 # Range: 0 -- 20 
playerName = "" # empty string 
playerScore = 0 
cpuScore = 0 
numGuesses = 0 
playerGuess = -1 

print("""
        +==============================+
        |                              |
        |        Guess the Number      |
        |              by              |
        |            Ryan K.           |
        |             2023             |
        +==============================+   
    """)

playerName = input("What should I call you?\nType your name and press enter.\n")
# VERIFY INPUT WHENEVER POSSIBLE! 
print(f"You want me to call you {playerName}.  Is that correct?")
isCorrect = input("Please type yes if correct, no if not correct.\n")
if isCorrect == "yes": 
    print(f"Ok {playerName}, let's continue!")
else: 
    playerName = input("What should I call you?\nType your name and press enter.\n")    