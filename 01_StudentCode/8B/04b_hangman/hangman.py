# Hangman Game by Ryan Kelley, v0.0 
import random 
words = 'cat bat rat sat mat fat pat apple banana potato tomato pasta fettucine linguine marinara dog moose mozzarella cheese energy missile plane bazooka phytoplankton mitochondria antidisestablishmentarianism supercalifragilisticexpiealadocius cow pig skunk lateral medial average explosion boom zoom doom loom mom dad baby brother sister equal equity hippopotamus platypus mushy mashed laugh egotistical'.split()

# VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE! 
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
     =======''', '''
    +---+
    O   |
        |
        |
     =======''', '''
    +---+
    O   |
    |   |
        |
     =======''', '''            
    +---+
    O   |
   /|   |
        |
     =======''', '''                             
    +---+
    O   |
   /|\  |
        |
     =======''', ''' 
    +---+
    O   |
   /|\  |
   /    |
     =======''', '''                       
    +---+
    O   |
   /|\  |
   / \  |
     =======''']

# Pick Word from List 
def getRandomWord(wordList): # Return a random word from the list. 
    wordIndex = random.randint(0, len(wordList) - 1)
    # len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.  
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord): 
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters: 
        print(eachLetter, end = ' ')
    print()
    
    blanks = '_' * len(secretWord)

    # Replace Blanks with Correct Letters
    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters: 
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed): 
    while True: 
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed: 
            print('Letter has been guessed already, try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz': 
            print('Please guess a LETTER from the English alphabet.')
        else:
            return guess 

def playAgain(): 
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith('y')

# Introduce the Game 
print('Welcome to Hangman by Ryan K.')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False 

# Main Game Loop 
while True: 
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord: 
        correctLetters = correctLetters + guess

        # Check To See If Winner, Winner Chicken Dinner 
        foundAllLetters = True
        for i in range(len(secretWord)): 
            if secretWord[i] not in correctLetters: 
                foundAllLetters = False
                break
        if foundAllLetters:  # if True:  
            print('Much wow! Very win!  Well done.')
            print('The secret word was ' + secretWord)
            gameIsDone = True 
    else: 
        missedLetters = missedLetters + guess 

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses and lost the game.') 
            print('You made this number of correct guesses ' + str(len(correctLetters)))
            print('The secret word was ' + secretWord)
            gameIsDone = True 

    if gameIsDone: 
        if playAgain():
            missedLetters = '' 
            correctLetters = ''
            gameIsDone = False 
            secretWord = getRandomWord(words)
        else:
            break 











# i = 0 
# while i < 100: 
#     word = getRandomWord(words)
#     print(word)
#     i += 1



