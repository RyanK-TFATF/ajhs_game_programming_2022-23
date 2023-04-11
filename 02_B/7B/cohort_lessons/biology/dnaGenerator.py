# DNA Generator, Ryan Kelley, v0.1

# Code Exuection Timing 
import time 
startTime = time.time()

# Random Number Generation Code
from random import randint 
# from modulename import functionname

# DNA Nucleotide Bases
dnaBases = ["A", "C", "G", "T"]

def generateDNASequence(): 
    # track number of bases created 
    basesGenerated = 0 

    basesRequested = int(input("How many bases do you need?\n"))

    # store the generated bases 
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += dnaBases[randint(0, 3)]
        basesGenerated += 1
    
    print(f"\nDNA Sequence: \n{dnaSequence}\n\n")
    return dnaSequence

dnaSequence = generateDNASequence()























































print("Execution Time: %s Seconds" % (time.time() - startTime))
