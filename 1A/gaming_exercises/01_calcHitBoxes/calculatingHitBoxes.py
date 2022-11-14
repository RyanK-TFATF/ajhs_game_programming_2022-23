# Calc. Hit Boxes, ryan kelley, 11-08-22 v0.2

# Hit Box Type 
hitBoxType = 0 # 2D Box = 1, 3D Box = 2 


# Hit Box A Measurements 
boxALength = 0
boxAWidth = 0
boxAHeight = 0

# Hit Box B Measurements 
boxBLength = 0
boxBWidth = 0
boxBHeight = 0

# Box A Area Calculations 
boxA2DArea = boxALength * boxAWidth
boxA3DArea = boxALength * boxAWidth * boxAHeight
# Box B Area Calculations 
boxB2DArea = boxBLength * boxBWidth
boxB3DArea = boxBLength * boxBWidth * boxBHeight

# Hit Box Choice Selection 
hitBoxType = int(input("Select the hit box type: 1 = 2D, 2 = 3D.\n"))

# Box A Measurements Input 
boxALength = int(input("Please enter the LENGTH for Box A.\n"))
boxAWidth = int(input("Please enter the WIDTH for Box A.\n"))
boxAHeight = int(input("Please enter the HEIGHT for Box A.\n"))
# Box B Measurements Input 
boxBLength = int(input("Please enter the LENGTH for Box B.\n"))
boxBWidth = int(input("Please enter the WIDTH for Box B.\n"))
boxBHeight = int(input("Please enter the HEIGHT for Box B.\n"))

# Verify Measurements 
print(f"Box A Measurements -- Length: {boxALength} Width: {boxAWidth} Height: {boxAHeight}\n")
print(f"Box B Measurements -- Length: {boxBLength} Width: {boxBWidth} Height: {boxBHeight}\n")
