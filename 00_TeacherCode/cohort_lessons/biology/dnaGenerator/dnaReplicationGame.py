# DNA Replication Game, Ryan Kelley, v0.3.01a 

# Import Entire Module
import time, datetime # BRING THE WHOLE TOOL BOX

# Import Specific Method from a Module 
from random import choice # BRING JUST THE TOOL YOU NEED

# Establish Pause Value
pause = int(input("This game will periodocally pause for you to read information.\nHow many seconds would you like for each pause?\nEnter a positive integer and press ENTER.\n"))

# Setup DNA Bases
dnaBases = ["A", "T", "G", "C"] # Adenine, Thymine, Guanine, Cytosine
rnaBases = ["T", "U", "C", "G"] # Thymine, Uracial, Cytosine, Guanine 

def gameIntro() -> None: 
    pass

def genDNA() -> str: 
    basesGenerated = 0 
    basesRequested = int(input("Please enter a positive integer value for the number of bases to generate.\n"))
    dnaSequence = ""    
    while basesGenerated < basesRequested: 
        dnaSequence += choice(dnaBases)
        basesGenerated += 1     
    return dnaSequence

def doTranscription(dnaSequence: str) -> tuple:     
    print("You need to enter the correct RNA sequence based on this DNA sequence.\n")
    print("\nRemember, the RNA base will have a U base to match with a T base from DNA.\n")
    print(f"The DNA Sequence is {dnaSequence}.\n")
    time.sleep(pause)
    # START TIMER 
    rnaStart = time.time()
    rnaSequence = input("Please type the correct RNA sequence with no spaces. Then press enter.\n")
    rnaStop = time.time() 
    rnaTime = rnaStop - rnaStart 
    return (rnaSequence, rnaTime) # Tuples are ORDERED (index), UNCHANGEABLE, Allows Duplicates

def verifySequence(dnaSequence: str, rnaSequence: str) -> bool: 
    isMatch = False 
    for rnaBase, dnaBase in zip(rnaSequence, dnaSequence): 
        if rnaBase == "U" and dnaBase != "T":            
            break
        elif rnaBase == "C" and dnaBase != "G":            
            break
        elif rnaBase == "T" and dnaBase != "A":            
            break
        elif rnaBase == "G" and dnaBase != "C":            
            break
        else: 
            isMatch = True 
    return isMatch 

def calcScore(rnaTime: float, dnaSequence: str) -> int: 
    score = 25000 # Base Score for Correct Match
    print(f"Base Score for Correct Sequence: {score}\n")
        
    # Time-Based Scoring Bonus
    # More Effecient to Start With Lowest -> Highest Possible Score?  Reverse the if-elif-else block order and change to >      
    if rnaTime < 1.0: 
        score += 100000 # HIGHEST POSSIBLE POINTS HERE 
    elif rnaTime < 3.0:        
        score += 90000
    elif rnaTime < 5.0: 
        score += 80000
    elif rnaTime < 7.0:
        score += 70000
    elif rnaTime < 10.0:
        score += 60000
    elif rnaTime < 15.0:
        score += 50000
    elif rnaTime < 25.0:
        score += 40000
    elif rnaTime < 40.0:
        score += 30000
    else: 
        score += 15000 # LOWEST POSSIBLE POINTS HERE
    print(f"\nYou earned {score} bonus points with a time of {rnaTime} seconds.\n")
    time.sleep(pause)
    # DNA Sequence Length Multiplier
    # If you want to give a bonus, make the multiplier > 1.0.  If you want to penalize, make the multipler < 1.0      
    scoreMulti = 0.0
    if len(dnaSequence) >= 50: 
        scoreMulti = 10.0
    elif len(dnaSequence) >= 35:
        scoreMulti = 7.0 
    elif len(dnaSequence) >= 25:
        scoreMulti = 5.0 
    elif len(dnaSequence) >= 10:
        scoreMulti = 2.0
    elif len(dnaSequence) >= 5:
        scoreMulti = 1.0
    else: 
        scoreMulti = 0.5
    score *= scoreMulti
    print(f"You earned a multiplier of {scoreMulti} based on a sequence length of {len(dnaSequence)} bases.\n") 
    print(f"Your final score for this round is {score}.\n")
    time.sleep(pause)
    return score 

def __main__():
    dna = genDNA()
    rna = doTranscription(dna)  
    if (verifySequence(dna, rna[0])): 
        print(calcScore(rna[1], dna))

__main__()

# To-Do List 
# __main__() loop for 3-5 attempts at the game. 
# Calculate final overall score. 
# Play Sounds and Display Images based on score. 
# Save Scores to File.  Generate Image or PDF file? 
