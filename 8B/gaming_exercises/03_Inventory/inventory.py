# 03_Inventory, Ryan Kelley, v0.0

p1inventory = [
    "steel sword", 
    "iron armor",
    "wood shield",
    "crossbow",
    "blue potion"
]

p2inventory = [
    "steel axe", 
    "iron underwear",
    "wood helmet",
    "rocket launcher",
    "hamberder"
]

# Defining a Function 
def displayInventory(inventory): # (PARAMETERS)
    print("You open your backpack and find the following:")
    for item in inventory:
        print(item)

# Call A Function 
#displayInventory(p1inventory)
#displayInventory(p2inventory)

rangedWeapons = [
    True, # Pistol 
    False, # Shotgun
    True, # Machinegun 
    False, # Rocketlauncher
    True # Flamethrower
]

def displayWeapons(weapons):
    weaponNumber = 0 
    while weaponNumber < len(weapons): 
        if weaponNumber == 0 and weapons[weaponNumber] == True:
            print("You are equipped with a pistol.")
        if weaponNumber == 1 and weapons[weaponNumber] == True:
            print("You are equipped with a shotgun.")
        if weaponNumber == 2 and weapons[weaponNumber] == True:
            print("You are equipped with a machinegun.")
        if weaponNumber == 3 and weapons[weaponNumber] == True:
            print("You are equipped with a rocket launcher.")
        if weaponNumber == 4 and weapons[weaponNumber] == True:
            print("You are equipped with a flame thrower.")
        weaponNumber += 1 
#displayWeapons(rangedWeapons)

def pickupItem(item, inventory): 
    print(f"You find the {item} and put it into your backpack.")
    inventory.append(item)

#displayInventory(p1inventory)
#pickupItem("moldy bread", p1inventory)
#displayInventory(p1inventory)

def hasItem(item, inventory): 
    if item in inventory: 
        return True 
    else: 
        return False 

def useItem(item, inventory): 
    if hasItem(item, inventory) == True: 
        print(f"You open your backpack, take out the {item}, and use it.")
        inventory.remove(item)
    else:
        print(f"You cannot seem to find the {item}.")

#useItem("blue potion", p1inventory)
#useItem("teleport scroll", p1inventory)

def clearInventory(inventory):
    inventory.clear()

displayInventory(p1inventory)
clearInventory(p1inventory)
displayInventory(p1inventory)



