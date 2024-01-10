# Ryan Kelley, DNA Replication Game, v0.0a 

# Import the time and datetime modules.  
import time, datetime 

# Import the choice method ONLY from the random module. 
from random import choice

# Create a list of the possible bases. 
dnaBases = ["A", "G", "C", "T"] # Adenine, Guanine, Cytosine, Thymine


# Game Introduction Function 
def gameIntro() -> None: 
    pass

# while loop to generate the DNA sequence. 
def genDNA() -> str:
    # Variable to count how many bases have been generated. 
    basesGenerated = 0

    # Variable to control while loop, allows user to specify the number of bases to generate. 
    requestedBases = int(input("How many DNA bases do you require in the sequence?  Type an integer value and press ENTER.\n"))
    
    # Create an empty string variable to store the DNA sequence. 
    dnaSequence = "" 
    
    while basesGenerated < requestedBases:         
        dnaSequence += choice(dnaBases) # [int(randint(0,3))] # This simulates picking the base at random and adding it to the sequence.  Start with 0 so the first element can be chosen! 
        basesGenerated += 1 # Increment the number of bases generated. 
    
    #print(f"\nGenerated DNA Sequence: \n{dnaSequence}\n\n")    
    return dnaSequence

def genRNA(dnaSequence: str) -> tuple: 
    print(f"The DNA Sequence is {dnaSequence}.\n")    
    print("You will now generate the RNA sequence.  Remember, Adenine on the DNA pairs with U on the RNA.\n")
    # Start Time
    rnaStart = time.time()
    rnaSequence = input("Please enter the correct RNA sequence.  Leave no spaces between bases.  When finished, push enter.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart 
    
    # End Time 
    return (rnaSequence, rnaTime)




def main():
    dnaSequence = genDNA() # Generate a DNA sequence and store it in the dnaSequence variable. 
        
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