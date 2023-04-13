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
    
    print(f"\nDNA Sequence: \n{dnaSequence}\n")
    return dnaSequence

dnaSequence = generateDNASequence()

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
            print("Unable to identify base during transcription.\n")
            exit()
    print(f"\nRNA Sequence: \n{rnaSequence}\n")
    return rnaSequence

rnaSequence = transcribeRNA(dnaSequence)

saveData = open("dnaData.txt", "w")
saveData.write(dnaSequence + "  " + str(time.time()) + "\n")
saveData.write(rnaSequence + "  " + str(time.time()) + "\n")
saveData.close()
# File Modes 
# "x" -- Creates a new file, exits with Error Message if exists.
# "a" -- Creates file if not there, appends to file if is there.
# "w" -- Creates file if not there, OVERWRITES if is there.
























































print("Execution Time: %s Seconds" % (time.time() - startTime))
