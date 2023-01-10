# 03_Inventory, Ryan Kelley, v0.4b

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
        return True 
    else:
        return False 
    
# call the hasItem() function for one item that IS in inventory
# and one that is NOT in the inventory. 
#hasItem("blue", doorKeys)
#hasItem("purple", doorKeys)

def useItem(item, inventory): 
    if hasItem(item, inventory) == True: 
        print(f"You open your backpack, remove the {item} and use it.")
        # Remove the first instance of the object from the inventory. 
        inventory.remove(item)
    else: 
        print(f"You cannot seem to find the {item} in your bag.")

#dispInventory(p1Inventory)
#useItem("blue mana potion", p1Inventory)
#dispInventory(p1Inventory)
#useItem("purple mana potion", p1Inventory)

# Add Items to Inventory 
def addItem(item, inventory): 
    print(f"You have picked up the {item} and put into your bag.")
    inventory.append(item)

#dispInventory(p1Inventory)
#addItem("gallon of milk", p1Inventory)
#dispInventory(p1Inventory)

def sortItems(inventory): 
    # Sort Alphabetically 
    inventory.sort()

#dispInventory(p1Inventory)
#sortItems(p1Inventory)
#dispInventory(p1Inventory)
