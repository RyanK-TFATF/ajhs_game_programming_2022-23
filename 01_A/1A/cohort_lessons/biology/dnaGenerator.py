# DNA Generator, Ryan Kelley, v0.2

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

