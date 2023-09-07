# Control Flow, ryan Kelley, v0.1 

# DECLARATIONS 
favColor = "Blue"
luckyNumber = 25
myGPA = 3.0
myAge = 66 
pineappleOnPizza = True 

# if Statement 
if luckyNumber > 30:
    print("Wow, what a great number!")

if favColor != "Green":
    print("Your favorite color stinks.")

# if-else Statement  
if myGPA >= 3.0: 
    print("Congratulations on making the honor roll!")
else: 
    print("You did not make the honor roll.")

# if-elif-else Statement 
# if myAge > 65: 
#     print("Please enjoy retirement!")
# elif myAge > 55: 
#     print("You have earned a $10,000 bonus!")
# elif myAge > 40: 
#     print("You have earned a $5,000 bonus.")
# else:
#     print("You have earned a $1,000 bonus.")
# 99% OF THE TIME CHECK FOR HIGHEST VALUES FIRST! 

if myAge > 40: 
    print("You have earned a $5,000 bonus.")
elif myAge > 55: 
    print("You have earned a $10,000 bonus!")
elif myAge > 65: 
    print("Please enjoy retirement!")    
else:
    print("You have earned a $1,000 bonus.")

# NESTED IF / ELIF / ELSE STATEMENTS    
if pineappleOnPizza == True: 
    print("You have strange tastes.  I bet you're old.")
    if myAge > 50:
        print("What was it like riding to school on a dinosaur?")                
    else: 
        print("Ok, you're still young enough to be cool.")
else:
    print("Ok good, you eat pizza like a normal human.")    
     