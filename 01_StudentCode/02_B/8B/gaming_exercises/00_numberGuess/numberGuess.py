# Select the secret number from a given range. 
# Player must guess the number. 
# Compare guess to the secret number. 
# What happens if the guess is wrong? 
    # Tell them the guess is wrong. 
    # Tell them the number of guesses left. 
    # Tell them if too high / too low. 
# What happens if the guess is right? 
    # Tell them guess is correct. 
    # Award a point. 
# What happens if the player runs out of guesses?
    # Tell player round has been lost. 
    # Award point to CPU. 
# Check to see if player or CPU has >= 3 points, if so they win.

import random # Import the random module to our code. 

# DECLARATIONS 
secretNumber = -1
playerGuess = -1 
playerScore = 0 
cpuScore = 0 
numGuesses = 0 
playerName = ""

print("""
        *~~~~~~~~~~~~~~~~~~~~~~~~~~~*
        |                           |
        |        Guess a Number     |
        |         ryan kelley       |
        |             2023          |
        *~~~~~~~~~~~~~~~~~~~~~~~~~~~*
      
      """)
