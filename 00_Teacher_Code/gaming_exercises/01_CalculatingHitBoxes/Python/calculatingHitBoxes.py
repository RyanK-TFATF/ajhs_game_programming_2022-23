# Calculating Hit Boxes, Ryan Kelley, 11/04/22, 12:01pm, v0.4

# Declare and Define Variables 
hitBoxType = 0 # 1 = 2D hitbox, 2 = 3D hitbox
# Select Type of Hit Box 
hitBoxType = int(input("Which type of hit box do you need to calculate? 1 = 2D or 2 = 3D\n"))

if hitBoxType == 1:
    print("You have selected a 2D hit box.\n")
elif hitBoxType == 2: 
    print("You have selected a 3D hit box.\n")
else: 
    print("ERROR: Invalid Hit Box Selection. Please Retry. \n")
    hitBoxType = int(input("Which type of hit box do you need to calculate? 1 = 2D or 2 = 3D\n"))

# HitBox A Variables 
hitBoxALength = 0
hitBoxAWidth = 0
hitBoxAHeight = 0

# hitBox B Variables 
hitBoxBLength = 0
hitBoxBWidth = 0
hitBoxBHeight = 0

# Input Hit Box A Measurements 
hitBoxAHeight = int(input("Please enter an integer value for hit box A height:\n"))
hitBoxAWidth = int(input("Please enter an integer value for hit box A width:\n"))
hitBoxALength = int(input("Please enter an integer value for hit box A length:\n"))

# Input Hit Box B Measurements 
hitBoxBAHeight = int(input("Please enter an integer value for hit box B height:\n"))
hitBoxBWidth = int(input("Please enter an integer value for hit box B width:\n"))
hitBoxBLength = int(input("Please enter an integer value for hit box B length:\n"))

# Hit Box 2D Area Calculations 
hitBoxA2DArea = hitBoxALength * hitBoxAWidth
hitBoxB2DArea = hitBoxBLength * hitBoxBWidth

# Hit Box 3D Area Calculations 
hitBoxA3DArea = hitBoxALength * hitBoxAWidth * hitBoxAHeight
hitBoxB3DArea = hitBoxBLength * hitBoxBWidth * hitBoxBHeight

# Verify Measurements
print(f"Box A -- Length: {hitBoxALength} Height: {hitBoxAHeight} Width: {hitBoxAWidth}\n")
print(f"Box B -- Length: {hitBoxBLength} Height: {hitBoxBHeight} Width: {hitBoxBWidth}\n")

# Print Areas on the Screen 
if hitBoxType == 1: 
    print(f"The area for 2D Hit Box A is {hitBoxA2DArea} pixels square.\n")
    print(f"The area for 2D Hit Box B is {hitBoxB2DArea} pixels square.\n")
elif hitBoxType == 2: 
    print(f"The area for 3D Hit Box A is {hitBoxA3DArea} pixels cubed.\n")
    print(f"The area for 3D Hit Box B is {hitBoxB3DArea} pixels cubed.\n")
else:
    print("ERROR: Could not calculate hit box area.\n")

# Determine Which Box Is Larger 
if hitBoxType == 1 and hitBoxA2DArea > hitBoxB2DArea: 
    print("2D Hit Box A is larger than 2D Hit Box B.\n")
    # Determine Difference Between Largest and Smallest Value 
    sizeDifference = hitBoxA2DArea - hitBoxB2DArea
    # Calculate Area Average
    boxAvg = (hitBoxA2DArea + hitBoxB2DArea) / 2
    print(f"The average is {boxAvg}.")
    # boxAvg = (hitBoxA2DArea + hitBoxA2DArea) * 0.5
    # Divide Difference By Average Area 
    divideDiffByAvg = sizeDifference / boxAvg
    percentDiff = divideDiffByAvg * 100 
    print(f"Box A is {percentDiff:.2f}% larger than Box B.")
elif hitBoxType == 1 and hitBoxA2DArea < hitBoxB2DArea: 
    print("2D Hit Box B is larger than 2D Hit Box A.\n")
    # Print the % difference in size.
elif hitBoxType == 1 and hitBoxA2DArea == hitBoxB2DArea:     
    print("2D Hit Box A is equal to 2D Hit Box B.\n")
    # Print the % difference in size.
# elif for 3D Hit Box A is larger. 
    # Print 3D Box A is larger. 
    # Print the % difference in size.
# elif for 3D Hit Box B is larger. 
    # Print 3D Box B is larger. 
    # Print the % difference in size.
# elif for 3D Hit Box A is equal to Hit Box B. 
    # Print they are equal. 
else:
    print("ERROR: Could not calculate hit box area.\n")





