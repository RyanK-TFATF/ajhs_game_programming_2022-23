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

def displayBoard(missedLetters, correctLetters, secretWord): 
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    # Display the Missed Letters 
    print('Missed Letters:', end = ' ' )
    for letter in missedLetters:
        print(letter, end = ' ')  
    print() 

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters: 
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            # The : character is used to SLICE strings into pieces. 
            # [:i] means slice from the start until index i
            # [i+1:] means slice from i+1 until the END 
            # [startingPoint:endingPoint]

    for letter in blanks: 
        print(letter, end = ' ')
    print()
    
        
            
      
      
    

                                   
# i = 0
# while i < 500000:
#     getRandomWord(wordList)
#     i += 1 


                
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 