# 03_Inventory, Ryan Kelley, v0.3a

'''
player1Inventory = [
    "red health potion", 
    "red health potion",
    "green apple", 
    "shield", 
    "axe", 
    "canteen of water",
    "50' of rope", 
    "torch",
    "clove of garlic"
    ]

player2Inventory = [
    "blue health potion", 
    "purple health potion",
    "giant turkey leg", 
    "broadsword", 
    "flintlock pistol", 
    "gun powder",
    "bullets", 
    "torch",
    "potato"
    ]

# Function Example 
def dispInventory(inventory): # Parameters are data needed for function.
    print("You have the following items in your bag:")
    for x in inventory:
        print(x)

# Call the Function 
dispInventory(player1Inventory)
dispInventory(player2Inventory)

rangedWeapons = [
    True, # pistol 
    False, # shotgun 
    True, # machinegun 
    True, # rocket launcher
    False # flame thrower 
]


def dispWeapons(weapons): 
    weaponCounter = 0 
    while weaponCounter < len(rangedWeapons):
        if weaponCounter == 0 and rangedWeapons[weaponCounter] == True:
            print("You are equipped with a pisol.")
        if weaponCounter == 1 and rangedWeapons[weaponCounter] == True:
            print("You are equipped with a shotgun.")
        if weaponCounter == 2 and rangedWeapons[weaponCounter] == True:
            print("You are equipped with a machinegun.")
        if weaponCounter == 3 and rangedWeapons[weaponCounter] == True:
            print("You are equipped with a rocket launcher.")
        if weaponCounter == 4 and rangedWeapons[weaponCounter] == True:
            print("You are equipped with a flamethrower.")
        weaponCounter += 1

dispWeapons(rangedWeapons)
'''
# Check If Item Exists in Inventory 
player3Inventory = [
    "holy water", 
    "wooden stake", 
    "garlic clove",
    "torch"
]

def hasItem(item, inventory): 
    if item in inventory:
        print("Great, you have the required item!")
        
    else:
        print("You are missing the required item.")
        

#hasItem("garlic clove", player3Inventory)
# Add two more function calls for different items. 

# Using Item 
def useItem(item, inventory): 
    if item in inventory:
        inventory.remove(item)
        print(f"You open your bag, pull out the {item} and use it.")
    else:
        print(f"You do not have the {item} to use.")
    

#print(player3Inventory)
useItem("holy water", player3Inventory)
useItem("potato", player3Inventory)
#print(player3Inventory)

# Picking Up Items 
def pickupItem(item, inventory): 
    inventory.append(item)
    print(f"You pickup the {item} and put it in your bag.")

#print(player3Inventory)
#pickupItem("potato", player3Inventory)
#print(player3Inventory)

def deathInventory(inventory): 
    print(f"The cold darkness of death slowly washes over you...")
    inventory.clear()

#print(player3Inventory)
#deathInventory(player3Inventory)
#print(player3Inventory)


