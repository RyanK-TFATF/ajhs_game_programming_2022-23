import random 
wordList = 'cat bat rat sat pat fat lunch dinner fettucine steak pasta potato tomato carrot phytoplankton spine skull cardiovascular respiratory integumentary endocrine blue orange green yellow silver purple'.split()
# .split() will split a string into separate elements, by default based on SPACE

# VARIABLE_NAMES that are ALL CAPS are CONSTANTS and not meant to change. 
HANGMAN_BOARD = ['''
    +----+
         |
         |
         |
         |
       =====''', '''
    +----+
    O    |
         |
         |
         |
       =====''', ''' 
    +----+
    O    |
    |    |
         |
         |
       =====''', ''' 
    +----+
    O    |
   /|    |
         |
         |
       =====''', ''' 
    +----+
    O    |
   /|\   |
         |
         |
       =====''', ''' 
    +----+
    O    |
   /|\   |
   /     |
         |
       =====''', ''' 
    +----+
    O    |
   /|\   |
   / \   |
         |
       ====='''] 

def getRandomWord(wordList):
    wordIndex = random.randint(0 , len(wordList) - 1)
    # len(listName) - 1 IS MOST COMMON WAY TO PREVENT INDEX OUT OF RANGE ERRORS
    #print(wordIndex)
    return wordList[wordIndex]

def displayBoard(incorrectLetters, correctLetters, secretWord): 
    print(HANGMAN_BOARD[len(incorrectLetters)])
    print(correctLetters) 
  

                                   
# i = 0
# while i < 500000:
#     getRandomWord(wordList)
#     i += 1 


                
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 