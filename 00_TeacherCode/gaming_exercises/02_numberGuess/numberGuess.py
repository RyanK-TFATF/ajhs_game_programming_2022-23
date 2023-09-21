# Pick the secret number from a range for the possible numbers (i.e. 0-10, 0-100, 100-200)
# Provide the player X number of guesses, based on range of numbers.  
# First player to score at least 3 points is declared the winner. 
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


# Guess a Number, Ryan Kelley, v0.0 
import random, tracemalloc, winsound
from PIL import Image 
tracemalloc.start()

# DECLARATIONS 
secretNumber = -1 # Range: 0 -- 20 
playerName = "" # empty string 
playerScore = 0 
cpuScore = 0 
numGuesses = 0 
playerGuess = -1 
difficulty = None
numAttempts = None
rangeMin = -1
rangeMax = -1 

loserSound = 'sfx/numberGuess/gameOver.wav'
winnerSound = None 

imageWin = Image.open('img/numberGuess/win.jpg')
imageLoss = None 


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

print("Next you will select a difficulty setting.\nEasy Mode: Range 0 to 10 with 5 guesses.\nNormal Mode: Range 0 to 20 with 5 guesses.\nHard Mode: Range 0 to 20 with 3 guesses.\n")
difficulty = input("Please type Easy, Normal, or Hard then press ENTER.\n")
if difficulty == "Easy":
    numAttempts = 5
    x = 0 
    y = 10 
elif difficulty == "Normal":
    numAttempts = 5
    x = 0 
    y = 20
elif difficulty == "Hard":
    numAttempts = 3
    x = 0 
    y = 30
else: 
    print("Difficulty not identified, defaulting to Normal.\n")
    numAttempts = 5
    x = 0 
    y = 20
   

# PLAYER GUESS 
print(f"You need to guess a number from {x} to {y}.  You have {numAttempts} guesses!\n")
      
while playerScore != 3 and cpuScore != 3: 
    #pass  Tells Python to skip this block without giving an error. 
    # GENERATE SECRET NUMBER
    secretNumber = random.randint(x, y) # INCLUSIVE
    print(secretNumber)
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}\n")
    numGuesses = 0 
    for guesses in range(numAttempts):         
        print(f"You have {numAttempts - numGuesses} remaining this round.\n")
        playerGuess = int(input("Think of your number, type it in and then push ENTER.\n"))
        print(f"You have picked {playerGuess}.  Let's see if it is a match!\n")
        if playerGuess == secretNumber: 
            playerScore += 1 
            print("A winner is you! It's a match!\n")
            break
        else:         
            if playerGuess < secretNumber: 
                print("Your guess is too low!\n")
            else: 
                print("Your guess is too high!\n")
        numGuesses += 1
            
    if playerGuess != secretNumber:
        print("You did not guess correctly before running out of guesses, the CPU wins.\n")
        winsound.PlaySound(loserSound, winsound.SND_FILENAME)
        cpuScore += 1

            

if playerScore >= 3:
    print("You scored three points first, well done!")
    imageWin.show() 
else:
    print("The CPU has scored three points first and defeated you.")
    imageLoss.show() 

print("Memory Usage: (Current, Peak)")
print(tracemalloc.get_traced_memory())
tracemalloc.stop()