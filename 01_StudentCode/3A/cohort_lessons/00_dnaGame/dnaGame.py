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
    # More Effecient to Start With Lowest -> Highest Possible Score?  
    # Reverse the if-elif-else block order and change to >  
    if time < 1.0: 
        score += 100000 # HIGHEST POSSIBLE POINTS HERE 
    elif time < 3.0:        
        score += 90000
    elif time < 5.0: 
        score += 80000
    elif time < 7.0:
        score += 70000
    elif time < 10.0:
        score += 60000
    elif time < 15.0:
        score += 50000
    elif time < 25.0:
        score += 40000
    elif time < 40.0:
        score += 30000
    else: 
        score += 25000 # LOWEST POSSIBLE POINTS HERE

    # DNA Sequence Length Multiplier
    # If you want to give a bonus, make the multiplier > 1.0
    # If you want to penalize, make the multipler < 1.0  
    if len(dnaSequence) >= 50: 
        score *= 10.0
    elif len(dnaSequence) >= 25:
        score *= 5.0 
    elif len(dnaSequence) >= 10:
        score *= 2.0
    elif len(dnaSequence) >= 5:
        score *= 1.25
    else: 
        score *= 0.5 
    return score 

dna = genDNA()
print(dna)

rna = genRNA(dna)  
print(rna)
print(checkSequence(dna, rna[0]))

