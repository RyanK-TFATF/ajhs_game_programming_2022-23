# 03_Loops, Ryan Kelley, v0.3a 
import random 
import time 
# while loop 
'''
loopCounter = 100 
while loopCounter >= 0:
    print(f"Loop Counter: {loopCounter}")
    loopCounter += -1 
while loopCounter < 100: 
    print(f"Loop Counter: {loopCounter}")
    if loopCounter == 75:
        break
    loopCounter += random.randint(1, 6)
''' 

# for loops 
colors = ["red", "orange", "yellow", "green", "blue"]
animals = ["platypus", "kookaburra", "velociraptor", "moose", "squirrel"] 
'''
for eachColor in colors: 
    print(eachColor)
    if eachColor == "green":
        print("I am so envious!")
for x in animals:
    print(x)
    if x == "velociraptor":
        print("Clever girl.")
'''

'''
# Nested Loops -- 
outerLoop = 0
innerLoop = 0
# Outer Loop 
for x in colors:
    print(f"Outer Loop Count: {outerLoop}")
    outerLoop += 1
    # Inner Loop
    time.sleep(1)
    for y in animals: 
        print(x, y) 
        print(f"Inner Loop: {innerLoop}")
        innerLoop +=1 
'''
for y in range(10):
    print(y)

for y in range(50, 100):
    print(y)

for y in range(1, 10000, 25):
    print(y)
