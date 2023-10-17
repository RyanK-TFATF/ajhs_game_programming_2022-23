# playerInventory = []

# while len(playerInventory) < 10: 
#     item = input("What item do you want to add to the inventory?\n")
#     playerInventory.append(item)

# playerInventory.sort()
# print(playerInventory)

# while len(playerInventory) > 5:
#     item = input("What item do you want to remove from the inventory?\n")
#     playerInventory.remove(item)

# playerInventory.sort()
# print(playerInventory)

#doorKeys = [
#     "red", 
#     "green", 
#     "yellow", 
#     "purple", 
#     "brown"
# ]

# key = input("Which color key do you need to unlock the door?\n")

# if key in doorKeys: 
#     print("You have the correct key!  The door unlocks.\n")
# else: 
#     print("You do not have that key.  The door remains locked.\n")

weaponList = [
    True, # sword    
    False, # flame thrower
    False, # gun that shoots more guns 
    True, # grappling hook 
    False, # missile launcher
    True, # teleporter beam 
    False # laser blaster
]

weaponNum = 0 
while weaponNum < len(weaponList):
    if weaponNum == 0 and weaponList[0] == True:  
        print("You are wielding a shiny sword.\n")
    if weaponNum == 1 and weaponList[1] == True:  
        print("You have a toasty flame thrower.\n")
    if weaponNum == 2 and weaponList[2] == True:  
        print("A gun that shoots more guns is in your backpack.\n")
    if weaponNum == 3 and weaponList[3] == True:  
        print("You can climb walls with this grappling hook.\n")
    if weaponNum == 4 and weaponList[4] == True:  
        print("A missile launcher is available to use.\n")
    if weaponNum == 5 and weaponList[5] == True:  
        print("The unique teleporter beam is in your hand.\n")
    if weaponNum == 6 and weaponList[6] == True:  
        print("You are wielding the alien blaster.\n")
    weaponNum += 1
     