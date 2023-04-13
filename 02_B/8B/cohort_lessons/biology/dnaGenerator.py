# DNA Generator, Ryan Kelley, v0.0 

# Code Execution Timing 
import time, datetime 
startTime = time.time() 

# Random Number Generation 
# from modulename import functionname 
from random import randint 

# DNA Bases
dnaBases = ["A", "C", "G", "T"] 

def generateDNASequence():
    # Bases Generated
    basesGenerated = 0 

    # Bases Requested
    basesRequested = int(input("How many bases do you need? Must be an integer!\n"))

    # Store the Bases
    dnaSequence = ""

    while basesGenerated <= basesRequested:
        dnaSequence += dnaBases[randint(0, 3)]
        basesGenerated += 1 

    print(f"DNA Sequence: \n{dnaSequence}\n")    

generateDNASequence()



print("Execution Time %s Seconds" % (time.time() - startTime))












