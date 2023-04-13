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

    while basesGenerated < basesRequested:
        dnaSequence += dnaBases[randint(0, 3)]
        basesGenerated += 1 

    print(f"DNA Sequence: \n{dnaSequence}\n")    
    return dnaSequence

dnaSequence = generateDNASequence()

def rnaTranscription(dnaSequence):
    rnaSequence = ""

    for eachBase in dnaSequence:
        if eachBase == "T":
            rnaSequence += "A"
        elif eachBase == "A":
            rnaSequence += "U"
        elif eachBase == "G":
            rnaSequence += "C"
        elif eachBase == "C":
            rnaSequence += "G"
        else:
            print("Transcription Error! Base unknown.\n")
            exit()
    print(f"RNA Sequence: \n{rnaSequence}\n")    
    return rnaSequence

rnaSequence = rnaTranscription(dnaSequence)

saveData = open("dna_rnaData.txt", "a")
saveData.write(dnaSequence + " " + str(datetime.datetime.now()) + "\n")
saveData.write(rnaSequence + " " + str(datetime.datetime.now()) + "\n")
saveData.close()
# File Modes 
# "x" -- CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR CODE
# "a" -- CREATES FILE, IF FILE EXISTS, ADD ON TO END OF FILE
# "w" -- CREATES FILE, IF FILE EXISTS, OVERWRITE IT 

print("Execution Time %s Seconds" % (time.time() - startTime))












