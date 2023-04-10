# Loot Box Cost Calculator, Ryan Kelley, v0.5b 
from random import randint
import time
# import sys, os for file access
# open file to save lootbox info. 

def main(): 
    
    # Simulation assumes that duplicate items will award crafting materials instead.  
    craftingMaterials = 0 

    # Rare Items
    numRare = int(input("How many rare items are available in your game?\n"))
    rareChance = int(input("What is the percentage chance of getting a rare item in the loot box?  Enter an integer number without a % sign..\n"))  
    rareItemsAvailable = createRareItems(numRare)
    rareItemsOpened = []    
    
    # Rare Guaranteed Packs?
    rareOpened = False # Used for tracking the guaranteed rare in a pack. 
    rareGuaranteed = int(input("Are you guaranteed at least one rare item per loot box? Enter 0 for No, 1 for yes.\n"))    
    if rareGuaranteed == 0:
        rareGuaranteed = False        
    elif rareGuaranteed == 1:
        rareGuaranteed = True

    # Uncommon Items
    numUncommon = int(input("How many uncommon items are available in your game?\n"))
    uncommonChance = int(input("What is the percentage chance of getting an uncommon item in the loot box?  Enter an integer number without a % sign..\n"))  
    uncommonItemsAvailable = createUncommonItems(numUncommon)
    uncommonItemsOpened = []
    
    # Common Items -- For this simlutation, we will assume any item that is not rare or uncommon is common, and do not ask for % chance.
    numCommon = int(input("How many common items are available in your game?\n"))        
    commonItemsAvailable = createCommonItems(numCommon)
    commonItemsOpened = []      
    
    # Loot Box Structure
    numItemsPerBox = int(input("How many items are in each box?\n"))           
    numItemsOpened = 0
    numBoxesOpened = 0 
    costPerBox = int(input("What is the cost per single loot box?  Round answer to the nearest dollar, do not include the $.\n"))


    while len(commonItemsAvailable) > len(commonItemsOpened) or len(uncommonItemsAvailable) > len(uncommonItemsOpened) or len(rareItemsAvailable) > len(rareItemsOpened):
        print(f"Length of commonItems available:  {len(commonItemsAvailable)} Length of commonItemsOpen: {len(commonItemsOpened)}\n")
        print(f"Length of uncommonItems available:  {len(uncommonItemsAvailable)} Length of uncommonItemsOpen: {len(uncommonItemsOpened)}\n")
        print(f"Length of rareItems available:  {len(rareItemsAvailable)} Length of rareItemsOpen: {len(rareItemsOpened)}\n")
        while numItemsOpened < numItemsPerBox: 
            itemRoll = randint(1, 100)       
        
            if rareGuaranteed == True and rareOpened == False:
                theItemIndex = randint(0, len(rareItemsAvailable) - 1)
                itemOpened = rareItemsAvailable[theItemIndex] 
                if itemOpened in rareItemsOpened:
                    craftingMaterials += 100
                else:                    
                    rareItemsOpened.append(itemOpened)            
                rareOpened = True
                numItemsOpened += 1            

            elif itemRoll <= rareChance:
                theItemIndex = randint(0, len(rareItemsAvailable) - 1)
                itemOpened = rareItemsAvailable[theItemIndex] 
                if itemOpened in rareItemsOpened:
                    craftingMaterials += 100
                else:                    
                    rareItemsOpened.append(itemOpened)                          
                numItemsOpened += 1      

            elif itemRoll > rareChance and itemRoll <= uncommonChance: 
                theItemIndex = randint(0, len(uncommonItemsAvailable) - 1)
                itemOpened = uncommonItemsAvailable[theItemIndex] 
                if itemOpened in uncommonItemsOpened:
                    craftingMaterials += 50
                else:                    
                    uncommonItemsOpened.append(itemOpened)              
                numItemsOpened += 1         

            else:
                theItemIndex = randint(0, len(commonItemsAvailable) - 1)
                itemOpened = commonItemsAvailable[theItemIndex]             
                if itemOpened in commonItemsOpened:
                    craftingMaterials += 25
                else:                    
                    commonItemsOpened.append(itemOpened)              
                numItemsOpened += 1           
        numBoxesOpened += 1
        numItemsOpened = 0 
       
             
    print(f"Crafting Materials Opened {craftingMaterials}\n")    
    print(f"Number of Boxes Opened {numBoxesOpened}\n")
    print(f"Total Cost of Boxes: ${numBoxesOpened * costPerBox:,}.\n")

# Common Item Functions 
def createCommonItems(num):
    # Test
    itemCount = 0 
    commonItems = []
    while len(commonItems) < num:
        commonItems.append("Common Item #" + str(itemCount))
        itemCount += 1
    #print(commonItems)
    return commonItems 

# Unommon Item Functions 
def createUncommonItems(num):
    # Test
    itemCount = 0 
    uncommonItems = []
    while len(uncommonItems) < num:
        uncommonItems.append("Uncommon Item #" + str(itemCount))
        itemCount += 1
    #print(uncommonItems)
    return uncommonItems

# Rare Item Functions 
def createRareItems(num):
    # Test
    itemCount = 0 
    rareItems = []
    while len(rareItems) < num:
        rareItems.append("Rare Item #" + str(itemCount))
        itemCount += 1
    #print(rareItems)
    return rareItems


main() 