# Dice Roll Module by Ryan Kelley, v1.0 
import random, time 

# Verified Working as of 12-13-23 
def rollDice(numRoll, sizeRoll): 
    count = 0 
    sum = 0 
    while count < numRoll:
        roll = random.randint(1, sizeRoll)                
        sum += roll 
        count += 1    
    return sum 

# Verified Working as of 12-13-23 
def dispDice(numRoll, sizeRoll): 
    count = 0 
    sum = 0 
    while count < numRoll:
        roll = random.randint(1, sizeRoll)
        print(f"Roll #{count}: {roll}\n")
        sum += roll 
        count += 1
    print(f"The sum is {sum}.\n")
    return sum 

# Verified Working as of 12-13-23 
def isExploding(roll, sizeRoll): 
    if roll == sizeRoll:
        print("This roll exploded!\n")
        isExploding = True         
    else: 
        isExploding = False             
    return isExploding
    

# Confirmed Working as of 12-13-23  
def isDouble(roll1, roll2):     
    if roll1 == roll2: 
        isDouble = True 
    else: 
        isDouble = False 
    return isDouble 



