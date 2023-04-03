# Loot Box Cost Calculator, Ryan Kelley, v0.2 
# import randint 
# import sys, os for file access
# open file to save lootbox info. 

def main(): 
    percentage = 100 
    craftingMaterials = 0 

    # Common Items
    numCommon = int(input("How many common items are available in your game?\n"))
    commonChance = float(input("What is the percentage chance of getting a common item in the loot box?  Enter as a decimal.\n"))    
    print(commonChance)
    # commonItemsAvailable = createCommonItems(numCommon)
    # commonItemsOpened = []

    # # Uncommon Items
    # numUncommon = int(input("How many uncommon items are available in your game?\n"))
    # uncommonChance = float(input("What is the percentage chance of getting an uncommon item in the loot box?  Enter as a decimal.\n"))
    # uncommonItems = createUncommonItems(numUncommon)
    # uncommonItemsOpened = []
    
    # # Rare Items
    # numRare = int(input("How many rare items are available in your game?\n"))
    # rareChance = float(input("What is the percentage chance of getting a rare item in the loot box?  Enter as a decimal.\n"))
    # rareItems = createRareItems(numRare)
    # rareItemsOpened = []
    
    # # Loot Box Structure
    # numItemsPerBox = int(input("How many items are in each box?\n"))
    # rareGuaranteed = -1
    # while rareGuaranteed != 0 or rareGuaranteed != 1:
    #     int(input("Are you guaranteed at least one rare item per loot box? Enter 0 for No, 1 for yes.\n"))
    #     if rareGuaranteed == 0:
    #         rareGuaranteed = False
    #     elif rareGuaranteed == 1:
    #         rareGuaranteed = True

    
    
    
    
    
    
    
    
    

def createCommonItems(num):
    # Test
    itemCount = 0 
    commonItems = []
    while len(commonItems) < num:
        commonItems.append("Common Item #" + str(itemCount))
        itemCount += 1
    print(commonItems)
    return commonItems 

def createUncommonItems(num):
    # Test
    itemCount = 0 
    uncommonItems = []
    while len(uncommonItems) < num:
        uncommonItems.append("Uncommon Item #" + str(itemCount))
        itemCount += 1
    print(uncommonItems)
    return uncommonItems

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