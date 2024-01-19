# DNA Replication Game, Ryan Kelley, v0.0a 

# Import Entire Module
import time, datetime # BRING THE WHOLE TOOL BOX

# Import Specific Method from a Module 
from random import choice # BRING JUST THE TOOL YOU NEED

dnaBases = ["A", "T", "G", "C"] # Adenine, Thymine, Guanine, Cytosine

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
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You need to enter the correct RNA sequence based on this DNA sequence.\n")
    print("Remember, the RNA base will have a U base to match with an A base from DNA.\n")
    # START TIMER 
    rnaStart = time.time()
    rnaSequence = input("Please type the correct RNA sequence with no spaces. Then press enter.\n").upper()
    rnaStop = time.time() 
    rnaTime = rnaStop - rnaStart 
    return (rnaSequence, rnaTime) # Tuples are ORDERED (index), UNCHANGEABLE, Allows Duplicates

def checkSequence(dnaSequence: str, rnaSequence: str) -> bool: 
    isMatch = False 
    for rnaBase, dnaBase in zip(rnaSequence, dnaSequence): 
        if rnaBase == "U" and dnaBase != "A":            
            break
        elif rnaBase == "C" and dnaBase != "G":            
            break
        elif rnaBase == "A" and dnaBase != "T":            
            break
        elif rnaBase == "G" and dnaBase != "C":            
            break
        else: 
            isMatch = True 
    return isMatch 

def calcScore(rnaTime: float, dnaSequence: str) -> int: 
    score = 0 
    if rnaTime < 1.0: 
        score += 10000 # HIGHEST POSSIBLE POINTS AWARDED HERE 
    elif rnaTime < 5.0:        
        score += 90000
    elif rnaTime < 10.0: 
        score += 80000
    elif rnaTime < 15.0:
        score += 70000
    elif rnaTime < 20.0:
        score += 60000
    elif rnaTime < 25.0:
        score += 50000
    else: 
        score += 25000 # LOWEST POSSIBLE POINTS AWARDED HERE

    # DNA Sequence Length Multiplier
    # If you want to give a bonus, make the multiplier > 1.0
    # If you want to penalize, make the multipler < 1.0  
    if len(dnaSequence) >= 25: 
        score *= 4.0
    elif len(dnaSequence) >= 20:
        score *= 3.0 
    elif len(dnaSequence) >= 15:
        score *=  2.0
    elif len(dnaSequence) >= 10:
        score *=  1.0
    else: 
        score *= 0.5 # Penalized for less than 10 bases.  
    return score 

def saveScore(dna: str, rna: str, rnaTime: float, score: int) -> None: 
    firstName = input("What is your first name?\n")
    lastName = input("What is your last name?\n")
    fullName = firstName + " " + lastName 

    # Saving Files Example 
    # STEP 1: Create the filename to use for your program. 
    fileName = "dnaReplicationScore" + fullName + ".txt"
    # My Example:  dnaReplicationScoreRyanKelley.txt 
    # STEP 2: Open the file 'into' a variable. 
    saveData = open(fileName, "a") # First Param = file name, Second Param = file mode.
    # Three Main File Modes 
    # "w" -- CREATE FILE, IF FILE EXISTS, OVERWRITE THE CONTENTS 
    # "a" -- CREATE FILE, IF FILE EXISTS, APPEND TO END OF FILE 
    # "x" -- CREATE FILE, IF FILE EXISTS, EXIT WITH ERROR MESSAGE 

    # STEP 3: Write the data to the file.  
    saveData.write(f"\nScore Generated On: {datetime.datetime.now()}\n")
    # SAVE THE PLAYER NAME 
    # SAVE THE DNA SEQUENCE TO THE FILE 
    # SAVE THE RNA SEQUENCE TO THE FILE 
    # SAVE THE TIME 
    # SAVE THE SCORE 

    # STEP 4: Close the file. 
    saveData.close()




# Function Calls 
dna = genDNA()
rna = doTranscription(dna)  

if checkSequence(dna, rna[0]):  
    score = calcScore(rna[1], rna[0])
    saveScore(dna, rna[0], rna[1], score)
else: 
    print("Your RNA sequence did not correctly match.  Try again.\n")



