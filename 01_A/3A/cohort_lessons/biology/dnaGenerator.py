# DNA Sequence Generator, ryan kelley, v0.2

# Execution Timer 
import time 
startTime = time.time()

# Setup Random Number Generator 
# from modulename import functionname 
from random import randint 

dnaBases = ["A", "C", "G", "T"] 

def generateDNASequence():
    basesGenerated = 0 # How many bases have we made?

    basesNeeded = int(input("How many bases do you need?  Enter an integer.\n"))

    dnaSequence = ""

    while basesGenerated < basesNeeded: 
        dnaSequence += dnaBases[randint(0, 3)]
        basesGenerated += 1
    
    print(f"\nGenerated DNA Sequence: \n{dnaSequence}\n")
    return dnaSequence 

def transcribeRNA(dnaSequence):
    rnaSequence = ""
    
    for eachBase in dnaSequence:
        if eachBase == "A":
            rnaSequence += "U"
        elif eachBase == "C":
            rnaSequence += "G"
        elif eachBase == "G":
            rnaSequence += "C"
        elif eachBase == "T":
            rnaSequence += "A"
        else:
            print("Error transcribing RNA.  Base not identified.")

    print(f"\nGenerated RNA Sequence: \n{rnaSequence}\n")
    return rnaSequence 

dnaSequence = generateDNASequence() 
transcribeRNA(dnaSequence)

















































print("Execution Time: %s Seconds" % (time.time() - startTime))