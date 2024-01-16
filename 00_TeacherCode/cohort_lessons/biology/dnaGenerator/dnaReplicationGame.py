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
    isMatch = True 
    print(f"isMatch: {isMatch}\n")        
    time.sleep(1)
    for eachBase in range(len(rnaSequence)): 
        print(f"Index {eachBase}\nDNA Sequence: {dnaSequence[eachBase]}\nRNA Sequence: {rnaSequence[eachBase]}\n")
        if rnaSequence[eachBase] == "U" and dnaSequence[eachBase] != "T":
            isMatch = False
            break
        elif rnaSequence[eachBase] == "C" and dnaSequence[eachBase] != "G":
            isMatch = False
            break
        elif rnaSequence[eachBase] == "T" and dnaSequence[eachBase] != "A":
            isMatch = False
            break
        elif rnaSequence[eachBase] == "G" and dnaSequence[eachBase] != "C":
            isMatch = False
            break
    print(f"isMatch: {isMatch}\n")        
    time.sleep(1)
    return isMatch 

def checkSequenceZip(dnaSequence: str, rnaSequence: str) -> bool: 
    isMatch = False 
    print(f"isMatch: {isMatch}\n")        
    time.sleep(1)
    for rnaBase, dnaBase in zip(rnaSequence[0], dnaSequence): 
        print(f"\nRNA Sequence: {rnaBase}\nDNA Sequence: {dnaBase}\n")
        if rnaBase == "U" and dnaBase != "T":
            isMatch = False
            break
        elif rnaBase == "C" and dnaBase != "G":
            isMatch = False
            break
        elif rnaBase == "T" and dnaBase != "A":
            isMatch = False
            break
        elif rnaBase == "G" and dnaBase != "C":
            isMatch = False
            break
    print(f"isMatch: {isMatch}\n")        
    time.sleep(1)
    return isMatch 

dna = genDNA()
# print(dna)

rna = genRNA(dna)  
# print(rna)

print(checkSequenceZip(dna, rna[0]))
