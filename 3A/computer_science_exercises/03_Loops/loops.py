# Loops, Ryan Kelley, v0.3a

# while loop -- Best used when the number of loops needed is NOT KNOWN 
'''
loopCounter = 0 
while loopCounter < 100: 
    print(f"This is iteration number {loopCounter}.")
    loopCounter += 1 # INCREMENT the loop counter. 

loopCounterTwo = 0 
while loopCounterTwo < 100: 
    if loopCounterTwo == 59:
        break
    print(loopCounterTwo)
    loopCounterTwo += 1

loopCounterThree = 100 
while loopCounterThree > 0:
    print(loopCounterThree)
    loopCounterThree += -1 
    if loopCounterThree == 70:
        continue
'''    
# for loops -- Used for iterating through lists and objects. 
'''
exampleFoods = ["bacon", "eggs", "waffles", "bagels", "coffee"]
for eachItem in exampleFoods: 
    print(eachItem)

exampleNumbers = [1, 2, -1, -2, 5, -5, 0, -10, 27, -99]
for z in exampleNumbers:
    if z % 2 == 0:
        print(f"{z} is even.")
    else:
        print(f"{z} is odd.")

for x in "archaeology":
    print(x)

for x in range(100): 
    print(x)

for y in range(-10, 10): # SPECIFY START AND STOP VALUES. 
    print(y)

for z in range(-100, 100, 10): # THIRD VALUE IS INCREMENT VALUE 
    print(z) 
''' 

# Nested Loops 
colors = ["garnet", "gold", "green", "blue", "purple"]
animals = ["cobra", "chicken", "platypus", "horse", "lemur"]
outerLoop = 0
innerLoop = 0 

# Outer Loop 
for x in colors: 
    # Inner Loop     
    print(f"Outer Loop Count: {outerLoop}")
    for z in animals: 
        print(x, z)
        innerLoop += 1
        print(f"Inner Loop Count: {innerLoop}")
    outerLoop += 1 
    
    






