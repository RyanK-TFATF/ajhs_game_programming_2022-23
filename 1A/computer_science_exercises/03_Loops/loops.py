# Loops, Ryan Kelley, v0.1b 

# Two Major Types: while loop and for loop 
# while loop - use when you DO NOT know how many times the loop will run
# for loop - use when you DO know how many times the loop will run 

# While Loops -- Musical Chairs 

loopCounter = 0 # YOU ALWAYS NEED A VARIABLE TO TRACK # OF LOOPS (ITERATIONS)
while loopCounter < 100: # CONDITIONAL STATEMENT TO START LOOP 
    print(f"This is iteration number {loopCounter}.")
    print(f"There are {100 - loopCounter} iterations remaining.")
    loopCounter += 1
print("The loop is now finished.")   

x = 0 
while x != 500: 
    print(f"X is {x}.")
    if x == 250:
        break
    x += 1
print("The loop has broken.")





    

