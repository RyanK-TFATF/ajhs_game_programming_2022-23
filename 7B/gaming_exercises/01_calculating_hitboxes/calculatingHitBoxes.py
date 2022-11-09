# Calc. Hit Boxes, Ryan Kelley, v0.4 7B 

# Hit Box Type
boxType = 0 # 2D Box = 1, 3D Box = 2 

# Select Hit Box Type 
boxType = int(input("Please select a hit box model.  Enter 1 for 2D, 2 for 3D.")) 

if boxType == 1:
    print("You have selected a 2D hit box model.")
elif boxType == 2:
    print("You have selected a 3D hit box model.")
else: 
    print("Error: Incorrect model type selected.")
    boxType = int(input("Please select a hit box model.  Enter 1 for 2D, 2 for 3D.")) 
  

# Hit Box A Measurements 
boxALength = 0 
boxAWidth = 0 
boxAHeight = 0 

# Hit Box B Measurements 
boxBLength = 0 
boxBWidth = 0 
boxBHeight = 0 

# Input Hit Box Measurements
boxALength = int(input("Please enter the LENGTH of box A.\n")) 
boxAWidth = int(input("Please enter the WIDTH of box A.\n")) 
boxAHeight = int(input("Please enter the HEIGHT of box A.\n")) 

boxBLength = int(input("Please enter the LENGTH of box B.\n")) 
boxBWidth = int(input("Please enter the WIDTH of box B.\n")) 
boxBHeight = int(input("Please enter the HEIGHT of box B.\n")) 

# 2D Hit Box Areas 
boxA2DArea = boxALength * boxAWidth
boxB2DArea = boxBLength * boxBWidth

# 3D Hit Box Area 
boxA3DArea = boxALength * boxAWidth * boxAHeight
boxB3DArea = boxBLength * boxBWidth * boxBHeight

# Verify Measurements 
print(f"Box A Length: {boxALength} Width: {boxAWidth} Height: {boxAHeight}\n")
print(f"Box B Length: {boxBLength} Width: {boxBWidth} Height: {boxBHeight}\n")

# Print Area Calculations 
print(f"Box A -- 2D Area: {boxA2DArea} 3D Area: {boxA3DArea} \n")
print(f"Box B -- 2D Area: {boxB2DArea} 3D Area: {boxB3DArea} \n")

