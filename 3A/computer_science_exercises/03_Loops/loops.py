# Loops, Ryan Kelley, v0.1c

# while loop -- Best used when the number of loops needed is NOT KNOWN 
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
    



