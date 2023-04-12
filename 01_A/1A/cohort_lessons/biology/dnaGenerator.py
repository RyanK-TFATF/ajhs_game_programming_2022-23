# DNA Generator, Ryan Kelley, v0.3

# Import Execution Timing Code 
import time 
startTime = time.time()


# Import the random module. 
from random import randint 
# from the random module, import ONLY the randint function.

dnaBases = ["A", "C", "G", "T"] # Adenine, Cytosine, Guanine, Thymine

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

#print(dnaSequence)

# Copy the Strand 
dnaCopy = ""

for eachBase in dnaSequence:
    if eachBase == "A":
        dnaCopy += "T"
    elif eachBase == "C":
        dnaCopy += "G"
    elif eachBase == "G":
        dnaCopy += "C"
    elif eachBase == "T":
        dnaCopy += "A"
    else: 
        print("Unable to identify base pair, please restart.\n")
        exit()

print(dnaSequence)
print(dnaCopy)

print("Execution Time %s Seconds" % (time.time() - startTime))