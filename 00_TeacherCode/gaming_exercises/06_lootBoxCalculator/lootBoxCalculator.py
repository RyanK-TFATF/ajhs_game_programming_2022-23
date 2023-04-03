# Loot Box Cost Calculator, Ryan Kelley, v0.1 

def main(): 
    numCommon = int(input("How many common items are available in your game?\n"))
    numUncommon = int(input("How many uncommon items are available in your game?\n"))
    numRare = int(input("How many rare items are available in your game?\n"))

    commonItems = createCommonItems(numCommon)
    uncommonItems = createUncommonItems(numUncommon)
    rareItems = createRareItems(numRare)
    print(commonItems)
    print(uncommonItems)
    print(rareItems)

def createCommonItems(num):
    # Test
    itemCount = 0 
    commonItems = []
    while len(commonItems) < num:
        commonItems.append("Common Item #" + str(itemCount))
        itemCount += 1
    print(commonItems)
    return commonItems 

# createCommonItems(5)

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