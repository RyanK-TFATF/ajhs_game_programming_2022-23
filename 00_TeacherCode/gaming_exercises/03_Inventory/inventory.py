# 03_Inventory, Ryan Kelley, v0.0 

p1Inventory = [    
    "silver health potion",     
    "blue mana potion",    
    "red apple",    
    "brown potato",    
    "bronze armor",    
    "bronze shield",    
    "steel helmet",    
    "torch",    
    "stone axe",    
    "large green emerald"
    ]

p2Inventory = [
    "band-aid",
    "broken pencil",
    "tissue with a booger in it",
    "moldy cheese", 
    "old tater tots"
]

# Functions in Python 
def dispInventory(inventory): # <-- FUNCTION SIGNATURE 
    # inventory is a PARAMETER.  
    print("You have the following items in your backpack:")
    for item in inventory: 
        print(item)

# CALL THE FUNCTION 
#dispInventory(p1Inventory)  # p1Inventory is the ARGUMENT. 
#dispInventory(p2Inventory)

weapons = [
    True, # chainsaw 
    False, # sword 
    False, # pistol 
    True, # machinegun 
    False # flamethrower
]

def displayWeapons(weaponList):
    weaponCounter= 0 
    while weaponCounter < len(weapons): 
        if weaponCounter == 0 and weapons[weaponCounter] == True:
            print("You are equipped with a chainsaw.")
        if weaponCounter == 1 and weapons[weaponCounter] == True:
            print("You are equipped with a sword.")
        if weaponCounter == 2 and weapons[weaponCounter] == True:
            print("You are equipped with a pistol.")
        if weaponCounter == 3 and weapons[weaponCounter] == True:
            print("You are equipped with a machinegun.")
        if weaponCounter == 4 and weapons[weaponCounter] == True:
            print("You are equipped with a flame thrower.")                
        weaponCounter += 1

weapons[1] = True 
weapons[4] = True 
#displayWeapons(weapons) 

doorKeys = [
    "red",
    "blue",
    "orange",
    "yellow",
    "silver"
]

def hasItem(item, inventory):
    if item in inventory: 
        print(f"You have the {item} key!  You may proceed.")
    else:
        print(f"You must continue searching for the {item} key.")
    
# call the hasItem() function for one item that IS in inventory
# and one that is NOT in the inventory. 
#hasItem("blue", doorKeys)
#hasItem("purple", doorKeys)

