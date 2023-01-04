# Loops, Ryan Kelley, v0.2a

# Two Major Types: while loop and for loop 
# while loop - use when you DO NOT know how many times the loop will run
# for loop - use when you DO know how many times the loop will run 

# While Loops -- Musical Chairs 

#loopCounter = 0 # YOU ALWAYS NEED A VARIABLE TO TRACK # OF LOOPS (ITERATIONS)
#while loopCounter < 100: # CONDITIONAL STATEMENT TO START LOOP 
#    print(f"This is iteration number {loopCounter}.")
#    print(f"There are {100 - loopCounter} iterations remaining.")
#    loopCounter += 1
#print("The loop is now finished.")   

#x = 0 
#while x != 500: 
#    print(f"X is {x}.")
#    if x == 250:
#        break
#    x += 1
#print("The loop has broken.")

# FOR Loops 
exampleFoods = ["bacon", "eggs", "waffles", "pancakes"]
exampleNumbers = [1, 5, -10, 0, 3, -2, 16, -33, 25, -74]

'''
for eachFood in exampleFoods: # Variable to use when looping. 
    print(f"We're having {eachFood} for breakfast!")
    if eachFood == "bacon":
        print("No thanks, I do not eat pork.")
    else:
        print(f"{eachFood} sounds delicious!")

for x in exampleNumbers:
    if x % 2 == 0:
        print(f"{x} is even!")
    else:
        print(f"{x} is odd!")
       
    if x > 0:
        print(f"{x} is positive!")
    elif x < 0: 
        print(f"{x} is negative!")
    else: 
        print(f"{x} is zero.")
'''
# Using Range 
for y in range(101):
    print(y)

# Provide Start / Ending Range 
for y in range(5, 100):
    print(y)

# Provide Start/End and Increment Value
for y in range(100, 1000, 10):  # Third value is increment value. 
    print(y)








    

