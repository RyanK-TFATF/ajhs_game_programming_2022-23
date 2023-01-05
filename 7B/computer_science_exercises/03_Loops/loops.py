# 03_Loops, Ryan Kelley, v0.2a
import random
# while loop -- 
'''
loopCounter = 0 
while loopCounter < 500: # CONDITIONAL STATEMENT -- If TRUE, run loop.
    print(f"This loop has performed {loopCounter} iterations.")
    # Exiting Loops with break 
    if loopCounter == 450:
        break
    loopCounter +=  random.randint(1, 6) 
print("END OF FIRST LOOP")
loopCounterTwo = 500
while loopCounterTwo > 0:
    print(f"Loop Counter: {loopCounterTwo}")
    loopCounterTwo += -1
'''

# for loops 
animals = ["cat", "platypus", "velociraptor", "moose", "squirrel"] 
colors = ["red", "orange", "yellow", "green", "blue"]

'''
for eachAnimal in animals: 
    print(eachAnimal)
    if eachAnimal == "velociraptor":
        print("Clever girl.")
    else:
        print("Aww, so cute.")
for eachColor in colors: 
    print(eachColor)
'''
# Nested For Loops 
# Outer Loop Starts Here
outerLoop = 0
innerLoop = 0

for x in colors: 
    print(f"Outer Loop Count: {outerLoop}")
    outerLoop += 1
    for y in animals: 
        print(x, y)
        innerLoop += 1
        print(f"Inner Loop Counter: {innerLoop}")






