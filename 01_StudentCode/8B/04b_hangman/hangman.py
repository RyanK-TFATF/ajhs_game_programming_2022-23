# Hangman Game by Ryan Kelley, v0.0 
import random 
words = 'cat bat rat sat mat fat pat apple banana potato tomato pasta fettucine linguine marina mozzarella cheese energy missile plane bazooka phytoplankton mitochondria antidisestablishmentarianism supercalifragilisticexpiealadocius cow pig skunk moose'.split()

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
    # FINISH THURSDAY 

# i = 0 
# while i < 100: 
#     word = getRandomWord(words)
#     print(word)
#     i += 1



