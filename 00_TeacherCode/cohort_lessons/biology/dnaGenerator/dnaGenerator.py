# Ryan Kelley, DNA Base Pair Generator and Transcriber, v0.3a 

# This block of code is used to measure execution time. 
import time 
startTime = time.time()

# Import the randint Method from the random module. 
from random import randint

dnaBases = ["A", "G", "C", "T"] # Adenine, Guanine, Cytosine, Thymine
rnaCodons = ["AUG", "TAG"]
# ATG is the START codon, TAG is one of the stop codons.  
# Codon information referenced here:  https://www.genome.gov/genetics-glossary/Codon and https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables#Inverse_DNA_codon_table

# while loop to generate the DNA sequence. 
def generateDNASequence():
    # Variable to count how many bases have been generated. 
    basesGenerated = 0

    # Variable to control while loop, allows user to specify the number of bases to generate. 
    requestedBases = int(input("How many DNA bases do you require in the sequence?  Type an integer value and press ENTER.\n"))
    
    # Create an empty string variable to store the DNA sequence. 
    dnaSequence = "" 
    
    while basesGenerated < requestedBases:         
        dnaSequence += dnaBases[int(randint(0,3))] # This simulates picking the base at random and adding it to the sequence.  Start with 0 so the first element can be chosen! 
        basesGenerated += 1 # Increment the number of bases generated. 
    
    print(f"\nGenerated DNA Sequence: \n{dnaSequence}\n\n")    
    return dnaSequence

# Copy the original DNA sequence using transcription rules. 
def transcribeRNA(baseSequence):
    rnaSequence = ""
    for eachBase in baseSequence: 
        if eachBase == "A":
            rnaSequence += "U"
        elif eachBase == "C":
            rnaSequence += "G"
        elif eachBase == "G":
            rnaSequence += "C"
        elif eachBase == "T":
            rnaSequence += "A"
        else:
            print("Error!  Transcription not possible due to unidentified base.\n")
        
    print(f"\nTranscribed DNA Sequence: \n{rnaSequence}\n\n")
    return rnaSequence

# Using a list for the codons allows for the use of a for loop to search for each codon. 
def translateRNA(rnaSequence):
    for i in range(0, len(rnaCodons)):
        if rnaSequence.find(rnaCodons[i]) == -1: # .find() returns -1 if not found. 
            print(f"The {rnaCodons[i]} codon was NOT found in the generated sequence.\n")
        else: 
            print(f"The {rnaCodons[i]} codon was found!  The first instance starts at index {rnaSequence.find(rnaCodons[i])}.\n") # Return the index of the first instance of the codon. 


def main():
    dnaSequence = generateDNASequence() # Generate a DNA sequence and store it in the dnaSequence0 variable. 
    rnaSequence = transcribeRNA(dnaSequence) # Transcribe a new DNA string using dnaSequence0 as the original. 
    translateRNA(rnaSequence) # Search dnaSequence0 for any instances of the codons defined above. 

main() 
print("Execution Time: %s seconds" % (time.time() - startTime))