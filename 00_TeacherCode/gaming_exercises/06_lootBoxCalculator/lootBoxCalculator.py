# Loot Box Cost Calculator, Ryan Kelley, v0.2 
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
    uncommonChance = float(input("What is the percentage chance of getting an uncommon item in the loot box?  Enter as a decimal.\n"))
    uncommonItems = createUncommonItems(numUncommon)
    uncommonItemsOpened = []
    
    # Rare Items
    numRare = int(input("How many rare items are available in your game?\n"))
    rareChance = float(input("What is the percentage chance of getting a rare item in the loot box?  Enter as a decimal.\n"))
    rareItems = createRareItems(numRare)
    rareItemsOpened = []
    
    # Are you guaranteed at least one rare item per loot box? 
    rareGuaranteed = int(input("Are you guaranteed at least one rare item per loot box? Enter 0 for No, 1 for yes.\n"))
    if rareGuaranteed != 0 or rareGuaranteed != 1:        
        rareGuaranteed = int(input("Are you guaranteed at least one rare item per loot box? Enter 0 for No, 1 for yes.\n"))
    if rareGuaranteed == 0:
        rareGuaranteed = False        
    elif rareGuaranteed == 1:
        rareGuaranteed = True
    
    # Loot Box Structure
    numItemsPerBox = int(input("How many items are in each box?\n"))           

    if randint(1,100) <= commonChance: 
        commonItemsOpened.append(commonItemsAvailable[randint(0, commonItemsAvailable.len())])
        print(commonItemsOpened)


# Common Item Functions 
def createCommonItems(num):
    # Test
    itemCount = 0 
    commonItems = []
    while len(commonItems) < num:
        commonItems.append("Common Item #" + str(itemCount))
        itemCount += 1
    print(commonItems)
    return commonItems 

# Unommon Item Functions 
def createUncommonItems(num):
    # Test
    itemCount = 0 
    uncommonItems = []
    while len(uncommonItems) < num:
        uncommonItems.append("Uncommon Item #" + str(itemCount))
        itemCount += 1
    print(uncommonItems)
    return uncommonItems

# Rare Item Functions 
def createRareItems(num):
    # Test
    itemCount = 0 
    rareItems = []
    while len(rareItems) < num:
        rareItems.append("Rare Item #" + str(itemCount))
        itemCount += 1
    print(rareItems)
    return rareItems


main() 