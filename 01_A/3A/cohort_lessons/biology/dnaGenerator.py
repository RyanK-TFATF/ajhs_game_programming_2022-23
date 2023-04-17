# DNA Sequence Generator, ryan kelley, v0.2
# Execution Timer 
import time, datetime
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
rnaSequence = transcribeRNA(dnaSequence)

#variableToSave = open(FILENAME, MODE)
# FILENAME should in " " and should have name and extenstion, ex: "myfile.txt"
# "r" READ-ONLY MODE
# "x" --CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR CODE 
# "w" -- CREATES FILE, IF FILE EXISTS, OVERWRITE CONTENTS
# "a" -- CREATES, IF FILE EXISTS, APPEND TO END OF FILE 
saveData = open("dnaData3A.txt", "a")
saveData.write("DNA Sequence\n" + dnaSequence + "\n" + str(datetime.datetime.now()) + "\n")
saveData.write("RNA Sequence\n" + rnaSequence + "\n" + str(datetime.datetime.now()) + "\n")
# Write the RNA Sequence to the file. 
saveData.close()


print("Execution Time: %s Seconds" % (time.time() - startTime))