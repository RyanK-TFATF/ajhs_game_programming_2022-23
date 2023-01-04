# Loops, Ryan Kelley, v0.1b 

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

