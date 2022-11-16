# Calc. Hit Boxes, ryan kelley, 11-08-22 v0.2

# Hit Box Type 
hitBoxType = 0 # 2D Box = 1, 3D Box = 2 
# Hit Box Choice Selection 
hitBoxType = int(input("Select the hit box type: 1 = 2D, 2 = 3D.\n"))
if hitBoxType == 1:
    print("2D Hit Box Model Selected. ")
elif hitBoxType == 2:
    print("3D Hit Box Model Selected. ")
else:
    print("ERROR: INCORRECT HIT BOX MODEL SELECTED.\n")
    hitBoxType = int(input("Select the hit box type: 1 = 2D, 2 = 3D.\n"))

# Hit Box A Measurements 
boxALength = 0
boxAWidth = 0
boxAHeight = 0

# Hit Box B Measurements 
boxBLength = 0
boxBWidth = 0
boxBHeight = 0

# Box A Measurements Input 
boxALength = int(input("Please enter the LENGTH for Box A.\n"))
boxAWidth = int(input("Please enter the WIDTH for Box A.\n"))
boxAHeight = int(input("Please enter the HEIGHT for Box A.\n"))
# Box B Measurements Input 
boxBLength = int(input("Please enter the LENGTH for Box B.\n"))
boxBWidth = int(input("Please enter the WIDTH for Box B.\n"))
boxBHeight = int(input("Please enter the HEIGHT for Box B.\n"))

# Box A Area Calculations 
boxA2DArea = boxALength * boxAWidth
boxA3DVol = boxALength * boxAWidth * boxAHeight
# Box B Area Calculations 
boxB2DArea = boxBLength * boxBWidth
boxB3DVol = boxBLength * boxBWidth * boxBHeight

# Verify Measurements 
print(f"Box A Measurements -- Length: {boxALength} Width: {boxAWidth} Height: {boxAHeight}\n")
print(f"Box B Measurements -- Length: {boxBLength} Width: {boxBWidth} Height: {boxBHeight}\n")

# Print Area Calculations 
if hitBoxType == 1:
    print(f"Hit Box A 2D Area: {boxA2DArea}")
    print(f"Hit Box B 2D Area: {boxB2DArea}")
elif hitBoxType == 2:
    print(f"Hit Box A Volume: {boxA3DVol}")
    print(f"Hit Box B Volume: {boxB3DVol}")
else:
    print("Error calculating hit box. Please restart the program.\n")

# Which box is larger?  If if / elif / else and determine which. 
if hitBoxType == 1 and boxA2DArea > boxB2DArea:
    print("Box A 2D area is greater than Box B 2D area.") 
    # Calculate the Difference Between Hit Boxes 
    boxDiff = boxA2DArea - boxB2DArea
    # Calculate the Average of the Box Areas 
    avgArea = (boxA2DArea + boxB2DArea) / 2 
    # Divide Average by Difference 
    diffDivByAvg = boxDiff / avgArea
    percentDiff = diffDivByAvg * 100 
    print(f"Box A is {percentDiff:.2f}% larger than Box B.")

elif hitBoxType == 1 and boxB2DArea > boxA2DArea:
    print("Box B 2D area is greater than Box A 2D area.") 

elif hitBoxType == 1 and boxB2DArea == boxA2DArea:
    print("Box B 2D area is equal to Box A 2D area.") 

elif hitBoxType == 2 and boxA3DVol > boxB3DVol:
    print("Box A volume is greater than Box B volume.") 

elif hitBoxType == 2 and boxB3DVol > boxA3DVol:
    print("Box B volume is greater than Box A volume.") 

elif hitBoxType == 2 and boxB3DVol == boxA3DVol:
    print("Box B volume is equal to Box A volume.") 
else: 
    print("ERROR: Unable to complete calculations. Please restart and try again.")

