# Ryan Kelley, 2022 code.org 6-12 Curriculum Development Manager Example Artifact, v1.0
# This code represents the revised code using lists created during Lesson 3 and Lesson 4 if needed.

# Import the random module to allow for random integer generation to simulate rolling the d4.
import random 

dnaBases = ["A", "G", "C", "T"] # Adenine, Guanine, Cytosine, Thymine

dnaCodons = ["ATG", "TAG", "GAT", "TTT", "AGC"]
# ATG is the START codon, TAG is one of the stop codons.  
# Codon information referenced here:  https://www.genome.gov/genetics-glossary/Codon and https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables#Inverse_DNA_codon_table

# Create an empty string variable to store the DNA sequence. 
dnaSequence = "" 

# Variable to count how many bases have been generated. 
basesGenerated = 0

# Variable to control while loop, allows user to specify the number of bases to generate. 
requestedBases = int(input("How many DNA bases do you require in the sequence?  Type an integer value and press ENTER.\n"))

# while loop to generate the DNA sequence. 
while basesGenerated < requestedBases: 
    dnaSequence += dnaBases[int(random.randint(0,3))] # This simulates picking the base at random and adding it to the sequence.  Start with 0 so the first element can be chosen! 
    basesGenerated += 1 # Increment the number of bases generated. 
    
print(f"\nGenerated DNA Sequence: \n{dnaSequence}\n\n") # Print the sequence to verify proper generation. 

# Using a list for the codons allows for the use of a for loop to search for each codon. 
for i in range(0, len(dnaCodons)):
    if dnaSequence.find(dnaCodons[i]) == -1: # .find() returns -1 if not found. 
        print(f"The {dnaCodons[i]} codon was NOT found in the generated sequence.\n")
    else: 
        print(f"The {dnaCodons[i]} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodons[i])}.\n") # Return the index of the first instance of the codon.  