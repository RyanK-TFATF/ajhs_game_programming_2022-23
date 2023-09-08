# Control Flow, Ryan Kelley, v0.0 
# DECLARATIONS

favColor = "green"
luckyNumber = 55 
myGPA = "potato"
myAge = 43
pineappleOnPizza = True 

# if Statements - Check for a condition to be True/False, do something if true. 
if favColor == "Green":
    print("I like your style.")

if luckyNumber > 100: 
    print("Big numbers for a big winner!") 

# if-else Statement -- Check for a condition, do something for True and False
if myGPA >= 3.0:
    print("Congratulations on making the honor roll!")
else: 
    print("Better luck next year.  Try to study more!")

if myGPA >= 3.0:
    print("Congratulations on making the honor roll!")
else: 
    print("Better luck next year.  Try to study more!")

# if - elif - else Statements -- Checks for multiple conditions
if myAge > 65:
    print("Congratulations on retiring!")
elif myAge > 50: 
    print("Congratulations, you have earned a bonus of $1000!")
else: 
    print("You are not old enough for a bonus.")
# 1 if, 1 else, any number of elif allowed.  

# Nested if - elif - else Statements 
if myAge > 15:
    print("You are eligible for a license!")
    if myGPA >= 3.5: 
        print("You qualify for a new car!")
    elif myGPA > 2.0:
        print("You qualify for $500 off a car!")
    else: 
        print("You get nothing!")
else: 
    print("You are not yet old enough to drive.")

# When doing if - elif - else statements, check for the highest values first!!!!
if myGPA > 1.5: 
    print("You are in danger of failing for the year.")
elif myGPA > 2.0: 
    print("You are on track to graduate.")
elif myGPA > 3.0:
    print("You qualify for some scholarship money!")
elif myGPA > 3.99:
    print("You qualify for Bright Futures 100 percent scholarship!")
else:
    print("GPA was not calculated.  Please try again.")