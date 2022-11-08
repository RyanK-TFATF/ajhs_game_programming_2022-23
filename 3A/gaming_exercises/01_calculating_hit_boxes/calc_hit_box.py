# Calculating Hit Boxes, Ryan Kelley, 11/04/22, 12:01pm, v0.3

# Declare and Define Variables 
hitBoxType = 0 # 1 = 2D hitbox, 2 = 3D hitbox

# HitBox A Variables 
hitBoxALength = 0
hitBoxAWidth = 0
hitBoxAHeight = 0

# hitBox B Variables 
hitBoxBLength = 0
hitBoxBWidth = 0
hitBoxBHeight = 0

# Hit Box 2D Area Calculations 
hitBoxA2DArea = hitBoxALength * hitBoxAWidth
hitBoxB2DArea = hitBoxBLength * hitBoxBWidth

# Hit Box 3D Area Calculations 
hitBoxA3DArea = hitBoxALength * hitBoxAWidth * hitBoxAHeight
hitBoxB3DArea = hitBoxBLength * hitBoxBWidth * hitBoxBHeight

# Select Type of Hit Box 
hitBoxType = int(input("Which type of hit box do you need to calculate? 1 = 2D or 2 = 3D\n"))

if hitBoxType == 1:
    print("You have selected a 2D hit box.\n")
elif hitBoxType == 2: 
    print("You have selected a 3D hit box.\n")
else: 
    print("ERROR: Invalid Hit Box Selection, Please Restart Program\n")

# Input Hit Box A Measurements 
hitBoxAHeight = int(input("Please enter an integer value for hit box A height:\n"))
hitBoxAWidth = int(input("Please enter an integer value for hit box A width:\n"))
hitBoxALength = int(input("Please enter an integer value for hit box A length:\n"))

# Input Hit Box B Measurements 
hitBoxBAHeight = int(input("Please enter an integer value for hit box B height:\n"))
hitBoxBWidth = int(input("Please enter an integer value for hit box B width:\n"))
hitBoxBLength = int(input("Please enter an integer value for hit box B length:\n"))

# Verify Measurements
print(f"Box A -- Length: {hitBoxALength} Height: {hitBoxAHeight} Width: {hitBoxAWidth}\n")
print(f"Box B -- Length: {hitBoxBLength} Height: {hitBoxBHeight} Width: {hitBoxBWidth}\n")








