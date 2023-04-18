# Ryan Kelley, DNA Base Pair Generator and Transcriber, v0.4a 

# This block of code is used to measure execution time. 
import time, datetime 
startTime = time.time()

# Import the randint Method from the random module. 
from random import randint

dnaBases = ["A", "G", "C", "T"] # Adenine, Guanine, Cytosine, Thymine
rnaCodons = ["AUG", "TAG"]
# ATG is the START codon, TAG is one of the stop codons.  
# Codon information referenced here:  https://www.genome.gov/genetics-glossary/Codon and https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables#Inverse_DNA_codon_table

# Codon Chart Protein Dictionary
codonChart = {
    "GGU": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine",
    "GAG": "Glutamic Acid",
    "GAA": "Glutamic Acid",
    "GAC": "Aspartic Acid",
    "GAU": "Aspartic Acid",
    "GCU": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",
    "GUU": "Valine",
    "GUC": "Valine",
    "GUA": "Valine",
    "GUG": "Valine",
    "UUU": "Phenlyalanine",
    "UUC": "Phenlyalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGA": "STOP",
    "UGG": "Tryptophan",
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",
    "CCU": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",
    "CAU": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutamine",
    "CAG": "Glutamine",
    "CGU": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Isoleucine",
    "AUG": "Methionine",
    "ACU": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",
    "AAU": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",
    "AGU": "Serine",
    "AGC": "Serine",
    "AGA": "Arginine",
    "AGG": "Arginine"
}

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
    
    #print(f"\nGenerated DNA Sequence: \n{dnaSequence}\n\n")    
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
        
    #print(f"\nTranscribed DNA Sequence: \n{rnaSequence}\n\n")
    return rnaSequence

# Using a list for the codons allows for the use of a for loop to search for each codon. 
def translateRNA(rnaSequence):
    for i in range(0, len(rnaCodons)):
        if rnaSequence.find(rnaCodons[i]) == -1: # .find() returns -1 if not found. 
            print(f"The {rnaCodons[i]} codon was NOT found in the generated sequence.\n")
        else: 
            print(f"The {rnaCodons[i]} codon was found!  The first instance starts at index {rnaSequence.find(rnaCodons[i])}.\n") # Return the index of the first instance of the codon. 



def main():
    dnaSequence = generateDNASequence() # Generate a DNA sequence and store it in the dnaSequence variable. 
    rnaSequence = transcribeRNA(dnaSequence) # Transcribe a new DNA string using dnaSequence as the original. 
    translateRNA(rnaSequence) # Search dnaSequence for any instances of the codons defined above. 
    
    # File Saving Example 
    fileName = "dnaData" + str(time.time()) + ".txt"
    saveData = open(fileName, "a")
    # FILENAME should be a legal file name in quotes.  "dnaData.txt"
    # File Modes
    # "x" -- CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR MSG.
    # "w" -- CREATES FILE, IF FILE EXISTS, OVERWRITE CONTENTS.
    # "a" -- CREATES FILES, IF FILE EXISTS, APPEND TO END OF FILE.
    saveData.write(dnaSequence + " " + str(datetime.datetime.now()) + "\n")
    saveData.write(rnaSequence + " " + str(datetime.datetime.now()) + "\n")
    saveData.close()

main() 
print("Execution Time: %s seconds" % (time.time() - startTime))