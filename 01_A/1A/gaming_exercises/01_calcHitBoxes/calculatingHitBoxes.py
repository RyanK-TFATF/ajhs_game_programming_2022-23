# Calculating 2D and 3D Hit Boxes, Ryan Kelley, v1.0a
import time

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

print("Hit Box Measurements are done using pixels as the unit.")
time.sleep(2)
# Box A Measurements Input 
boxALength = int(input("Please enter the LENGTH for Box A.\n"))
boxAWidth = int(input("Please enter the WIDTH for Box A.\n"))
boxAHeight = int(input("Please enter the HEIGHT for Box A.  Enter 0 if 2D hit box.\n"))
# Box B Measurements Input 
boxBLength = int(input("Please enter the LENGTH for Box B.\n"))
boxBWidth = int(input("Please enter the WIDTH for Box B.\n"))
boxBHeight = int(input("Please enter the HEIGHT for Box B. Enter 0 if 2D hit box.\n"))

# Box A Area Calculations 
boxAArea = boxALength * boxAWidth
boxAVolume = boxALength * boxAWidth * boxAHeight
# Box B Area Calculations 
boxBArea = boxBLength * boxBWidth
boxBVolume = boxBLength * boxBWidth * boxBHeight

# Verify Measurements 
print(f"Box A Measurements -- Length: {boxALength} Width: {boxAWidth} Height: {boxAHeight}\n")
print(f"Box B Measurements -- Length: {boxBLength} Width: {boxBWidth} Height: {boxBHeight}\n")
time.sleep(2)

# Print Area or Volume Calculations 
if hitBoxType == 1:
    print(f"Hit Box A Area: {boxAArea} pixels squared.")
    print(f"Hit Box B Area: {boxBArea} pixels squared.")
elif hitBoxType == 2:
    print(f"Hit Box A Volume: {boxAVolume} pixels cubed.")
    print(f"Hit Box B Volume: {boxBVolume} pixels cubed.")
else:
    print("Error calculating hit box. Please restart the program.\n")
time.sleep(2)

# Which box is larger?  If if / elif / else and determine which. 
if hitBoxType == 1 and boxAArea > boxBArea:
    print("Box A area is greater than Box B area.") 
    # Calculate the Difference Between Hit Boxes 
    boxDiff = boxAArea - boxBArea
    # Calculate the Average of the Box Areas 
    avgArea = (boxAArea + boxBArea) / 2 
    # Divide Average by Difference 
    diffDivByAvg = boxDiff / avgArea
    percentDiff = diffDivByAvg * 100 
    print(f"Box A is {percentDiff:.2f}% larger than Box B.")
elif hitBoxType == 1 and boxBArea > boxAArea:
    print("Box B area is greater than Box A area.") 
    boxDiff = boxBArea - boxAArea
    avgArea = (boxAArea + boxBArea) / 2 
    diffDivByAvg = boxDiff / avgArea
    percentDiff = diffDivByAvg * 100 
    print(f"Box B is {percentDiff:.2f}% larger than Box A.")
elif hitBoxType == 1 and boxBArea == boxAArea:
    print("Box B area is equal to Box A area.") 
    # Boxes are equal no need to calculate difference. 
elif hitBoxType == 2 and boxAVolume > boxBVolume:
    print("Box A volume is greater than Box B volume.") 
    boxDiff = boxAVolume - boxBVolume
    avgArea = (boxAVolume + boxBVolume) / 2 
    diffDivByAvg = boxDiff / avgArea
    percentDiff = diffDivByAvg * 100 
    print(f"Box A is {percentDiff:.2f}% larger than Box B.")
elif hitBoxType == 2 and boxBVolume > boxAVolume:
    print("Box B volume is greater than Box A volume.") 
    boxDiff = boxBVolume - boxAVolume
    avgArea = (boxAVolume + boxBVolume) / 2 
    diffDivByAvg = boxDiff / avgArea
    percentDiff = diffDivByAvg * 100 
    print(f"Box A is {percentDiff:.2f}% larger than Box B.")    
elif hitBoxType == 2 and boxBVolume == boxAVolume:
    print("Box B volume is equal to Box A volume.") 
    # Boxes are equal, no need to calculate difference. 
else: 
    print("ERROR: Unable to complete calculations. Please restart and try again.")

