# Calc. Hit Boxes, ryan kelley, v0.1 11-07-22 13:57 

# Hit Box Type 
boxType = 0 # 1 = 2D Box, 2 = 3D Box 

# Determine Hit Box Type 
boxType = int(input("Please select a hit box type.  1 = 2D box, 2 = 3D box.\n"))

if boxType == 1:
    print("You have chosen a 2D hit box.\n")
elif boxType == 2:
    print("You have chosen a 3D hit box.\n")
else:
    print("Invalid box selection, please try again.\n")
    boxType = int(input("Please select a hit box type.  1 = 2D box, 2 = 3D box.\n"))

# Box A
boxALength = 0 
boxAWidth = 0 
boxAHeight = 0 

# Box B
boxBLength = 0 
boxBWidth = 0 
boxBHeight = 0 

# Box A Measurements 
boxALength = int(input("Please enter an integer value for Box A Length.\n"))
boxAWidth = int(input("Please enter an integer value for Box A Width.\n"))
boxAHeight = int(input("Please enter an integer value for Box A Height.\n"))

# Box B Measurements 
boxBLength = int(input("Please enter an integer value for Box B Length.\n"))
boxBWidth = int(input("Please enter an integer value for Box B Width.\n"))
boxBHeight = int(input("Please enter an integer value for Box B Height.\n"))

# Box A Area Calcs. 
boxA2D = boxAWidth * boxALength
boxA3D = boxAWidth * boxALength * boxAHeight

# Box B Area Calcs. 
boxB2D = boxBWidth * boxBLength
boxB3D = boxBWidth * boxBLength * boxBHeight

# Verify Measurements 
print(f"Box A Measurements --  Height: {boxAHeight} Width: {boxAWidth} Length: {boxALength}")
print(f"Box B Measurements --  Height: {boxBHeight} Width: {boxBWidth} Length: {boxBLength}")

# Print Areas for Box A and Box B. 
if boxType == 1:
    print(f"Box A -- 2D Area: {boxA2D} Box B 2D Area: {boxB2D}")
elif boxType == 2:
    print(f"Box A -- 3D Area: {boxA3D} Box B 3D Area: {boxB3D}")
else:
    print("Something has gone terribly wrong, please restart the program.\n")
    quit()

# Compare Which Is Larger, Print the % Difference 
if boxType == 1 and boxA2D > boxB2D:
    print("Box A 2D is larger than Box B 2D.")
    # Determine the Difference Between Larger Hit Box and Smaller Hit Box
    boxDiff = boxA2D - boxB2D
    # Calculate Average Area 
    avgArea = (boxA2D + boxB2D) / 2 
    # Divide Difference by Average
    diffDivByAvg = boxDiff / avgArea 
    # Convert to a Percentage
    percentDiff = diffDivByAvg * 100 
    print(f"Box A 2D is {percentDiff:.2f}% larger than Box B.")

elif boxType == 1 and boxB2D > boxA2D:
    print("Box B 2D is larger than Box A 2D.")
elif boxType == 1 and boxA2D == boxB2D:
    print("Box A 2D is equal to Box B 2D.")
elif boxType == 2 and boxA3D > boxB3D:
    print("Box A 3D is larger than Box B 3D.")
elif boxType == 2 and boxB3D > boxA3D:
    print("Box B 3D is larger than Box B 3D.")
elif boxType == 2 and boxA3D == boxB3D:
    print("Box A 3D is equal to Box B 3D.")
else: 
    print("Hit Box Type still not identified correctly.  Please restart the program.")


