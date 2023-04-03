# Loot Box Cost Calculator, Ryan Kelley, v0.4 
from random import randint
# import sys, os for file access
# open file to save lootbox info. 

def main(): 
    
    craftingMaterials = 0 

    # Common Items
    numCommon = int(input("How many common items are available in your game?\n"))
    commonChance = int(input("What is the percentage chance of getting a common item in the loot box?  Enter an integer number without a % sign..\n"))    
    
    commonItemsAvailable = createCommonItems(numCommon)
    commonItemsOpened = []

    # Uncommon Items
    numUncommon = int(input("How many uncommon items are available in your game?\n"))
    uncommonChance = int(input("What is the percentage chance of getting an uncommon item in the loot box?  Enter an integer number without a % sign..\n"))  
    uncommonItemsAvailable = createUncommonItems(numUncommon)
    uncommonItemsOpened = []
    
    # Rare Items
    numRare = int(input("How many rare items are available in your game?\n"))
    rareChance = int(input("What is the percentage chance of getting a rare item in the loot box?  Enter an integer number without a % sign..\n"))  
    rareItemsAvailable = createRareItems(numRare)
    rareItemsOpened = []
    
    # Are you guaranteed at least one rare item per loot box? 
    rareOpened = False
    rareGuaranteed = int(input("Are you guaranteed at least one rare item per loot box? Enter 0 for No, 1 for yes.\n"))    
    if rareGuaranteed == 0:
        rareGuaranteed = False        
    elif rareGuaranteed == 1:
        rareGuaranteed = True
    #print(rareGuaranteed)
    
    # Loot Box Structure
    numItemsPerBox = int(input("How many items are in each box?\n"))           
    numItemsOpened = 0
    numBoxesOpened = 0 
    costPerBox = int(input("What is the cost per single loot box?  Round answer to the nearest dollar, do not include the $.\n"))


    while numItemsOpened <= numItemsPerBox: 
        itemRoll = randint(1, 100)       
        
        if rareGuaranteed == True and rareOpened == False:
            theItemIndex = randint(0, len(rareItemsAvailable) - 1)
            itemOpened = rareItemsAvailable[theItemIndex] 
            rareItemsOpened.append(itemOpened)
            #print(rareItemsOpened)
            rareOpened = True
        
        if itemRoll <= rareChance:
            theItemIndex = randint(0, len(rareItemsAvailable) - 1)
            itemOpened = rareItemsAvailable[theItemIndex]             
            rareItemsOpened.append(itemOpened)            
            numItemsOpened += 1      

        if itemRoll <= uncommonChance: 
            theItemIndex = randint(0, len(uncommonItemsAvailable) - 1)
            itemOpened = uncommonItemsAvailable[theItemIndex] 
            uncommonItemsOpened.append(itemOpened)            
            numItemsOpened += 1           

        if itemRoll <= commonChance: 
            theItemIndex = randint(0, len(commonItemsAvailable) - 1)
            itemOpened = commonItemsAvailable[theItemIndex]             
            commonItemsOpened.append(itemOpened)
            numItemsOpened += 1           
    
    
    
    print(commonItemsOpened)
    print(uncommonItemsOpened)
    print(rareItemsOpened)            
    print(f"Number of Boxes Opened {numBoxesOpened}")

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