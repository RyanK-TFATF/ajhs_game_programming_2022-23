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

def genRNA(dnaSequence: str) -> tuple: 
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You need to enter the correct RNA sequence based on this DNA sequence.\n")
    print("Remember, the RNA base will have a U base to match with an A base from DNA.\n")
    # START TIMER 
    rnaStart = time.time()
    rnaSequence = input("Please type the correct RNA sequence with no spaces. Then press enter.\n")
    rnaStop = time.time() 
    rnaTime = rnaStop - rnaStart 
    return (rnaSequence, rnaTime) # Tuples are ORDERED (index), UNCHANGEABLE, Allows Duplicates

def checkSequence(dnaSequence: str, rnaSequence: str) -> bool: 
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

def calcScore(time: float, dnaSequence: str) -> int: 
    score = 0 
    if time < 1.0: 
        score += 10000 # HIGHEST POSSIBLE POINTS AWARDED HERE 
    elif time ?:        
        score += ?
    elif time ?: 
        score += ?
    elif time ?:
        score += ?
    elif time ?:
        score += ?
    else: 
        # LOWEST POSSIBLE POINTS AWARDED HERE

    # DNA Sequence Length Multiplier
    # If you want to give a bonus, make the multiplier > 1.0
    # If you want to penalize, make the multipler < 1.0  
    if len(dnaSequence) >= 25: 
        score *= 2.0
    elif len(dnaSequence) >= ?:
        score *= ? 
    elif len(dnaSequence) >= ?:
        score *= ? 
    else: 
        score *= ? 
    return score 

dna = genDNA()
print(dna)

rna = genRNA(dna)  
print(rna)
print(checkSequence(dna, rna[0]))

