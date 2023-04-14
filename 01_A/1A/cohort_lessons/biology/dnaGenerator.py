# DNA Generator, Ryan Kelley, v0.3

# Import Execution Timing Code 
import time, datetime  
startTime = time.time()


# Import the random module. 
from random import randint 
# from the random module, import ONLY the randint function.

dnaBases = ["A", "C", "G", "T"] # Adenine, Cytosine, Guanine, Thymine

def generateDNASequence():
# Bases Generated
    basesGenerated = 0 

    # Bases Requested
    basesRequested = 0 
    basesRequested = int(input("TYPE A STRING HERE TO ASK FOR NUMBER OF BASES.\n"))
    #print(basesRequested)

    # Store the Generated Bases
    dnaSequence = ""

    # Generate the Bases
    while basesGenerated < basesRequested: 
        dnaSequence += dnaBases[randint(0, 3)]
        basesGenerated += 1
    print(f"DNA Sequence: \n{dnaSequence}\n")
    return dnaSequence

dnaSequence = generateDNASequence()

def transcribeRNA(dnaSequence):
    # Copy the Strand 
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
            print("Unable to identify base pair, please restart.\n")
            exit()
    print(f"RNA Sequence: \n{rnaSequence}\n")
    return rnaSequence

rnaSequence = transcribeRNA(dnaSequence)

saveData = open("dnaData1A.txt", "a")
# FILENAME should be a legal file name in quotes.  "dnaData.txt"
# File Modes
# "x" -- CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR MSG.
# "w" -- CREATES FILE, IF FILE EXISTS, OVERWRITE CONTENTS.
# "a" -- CREATES FILES, IF FILE EXISTS, APPEND TO END OF FILE.
saveData.write(dnaSequence + " " + str(datetime.datetime.now()) + "\n")
saveData.write(rnaSequence + " " + str(datetime.datetime.now()) + "\n")
saveData.close()


print("Execution Time %s Seconds" % (time.time() - startTime))