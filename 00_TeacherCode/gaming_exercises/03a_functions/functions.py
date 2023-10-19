# Functions, 10-18-23, Ryan Kelley 
import random
def functionName(): # Function Signature 
    print("What is your name?\n")
    name = input("Please type it and press enter.\n")
    print(f"Hello, {name}.\n")

# Call The Function 
#functionName() 

def happyBirthday(numTimes, age):
    count = 0 
    while count < numTimes: 
        print("Happy Birthday!\n")
        count += 1
    print(f"Wow, you're {age} years old!\n")
    

#happyBirthday(10, 55) 

def functionWithReturn(num1, num2): 
    sum = num1 + num2
    quotient = sum / 5
    return quotient # return immediately exits a function. 

def functionWithoutReturn(num1, num2): 
    sum = num1 + num2
    quotient = sum / 5
    print(quotient)

example = functionWithoutReturn(5, 10)
print(example)

def rollDice(num, size):
    numRolled = 0
    sum = 0
    while numRolled < num:
        roll = random.randint(1, size) 
        sum += roll
        numRolled += 1
        print(f"Roll #: {numRolled}\nResult: {roll}\nSum: {sum}")
        
    print(sum)
    return sum

#rollDice(5, 3)
#rollDice(5, 25)

def rollStat(): 
    rolls = []
    count = 0
    while count < 4:
        rolls.append(rollDice(1, 6))
    print(rolls)
    
rollStat()

