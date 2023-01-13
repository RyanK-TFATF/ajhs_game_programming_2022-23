# 03_Inventory, Ryan Kelley, v0.1a 

p1inventory = [
    "iron sword", 
    "steel helmet", 
    "moldy bread", 
    "canteen", 
    "blue key"
]

p2inventory = [

    "iron axe", 
    "steel shield", 
    "moldy cheese", 
    "cup of water", 
    "green key"
]

# Defining a Function 
def displayInventory(inventory):
    print("Inside your backpack are the following items:")
    for item in inventory: 
        print(item)

# Call the Function 
#displayInventory(p1inventory)
#displayInventory(p2inventory)

# List of Booleans to Represent Weapons
weapons = [
    True, # Pistol  
    False, # Sword 
    False, # Machinegun 
    True, # Rocketlauncher 
    False # Alien Blaster Rifle 
]

def displayWeapons(weapons): 
    weaponNumber = 0 
    while weaponNumber < len(weapons): 
        if weaponNumber == 0 and weapons[weaponNumber] == True: 
            print("You are equipped with a pistol.")
        if weaponNumber == 1 and weapons[weaponNumber] == True: 
            print("You are equipped with a sword.")
        if weaponNumber == 2 and weapons[weaponNumber] == True: 
            print("You are equipped with a machinegun.")
        if weaponNumber == 3 and weapons[weaponNumber] == True: 
            print("You are equipped with a rocket launcher.")        
        if weaponNumber == 4 and weapons[weaponNumber] == True: 
            print("You are equipped with an alien blaster rifle.")
        weaponNumber += 1

#displayWeapons(weapons)

# Adding Items to Inventory 
def pickupItem(item, inventory): 
    inventory.append(item)
    print(f"You pickup the {item} and place it in your bag.")

#displayInventory(p1inventory)
#pickupItem("yellow banana", p1inventory)
#displayInventory(p1inventory)

def hasItem(item, inventory): 
    if item in inventory:
        return True
    else:
        return False 

# Using Items (Remove from Inventory)
def useItem(item, inventory): 
    if hasItem(item, inventory) == True: 
        print(f"You open your bag, remove the {item}, and use it.")
        inventory.remove(item) # Removes the FIRST item that matches. 
    else: 
        print(f"You cannot seem to find the {item}.")     

#displayInventory(p1inventory)
#useItem("moldy bread", p1inventory)
#displayInventory(p1inventory)
#useItem("green potato", p1inventory)

def clearInventory(inventory): 
    inventory.clear()

#displayInventory(p1inventory)
#clearInventory(p1inventory)
#displayInventory(p1inventory)




