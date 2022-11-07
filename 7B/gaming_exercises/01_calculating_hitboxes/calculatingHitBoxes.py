# Calc. Hit Boxes, Ryan Kelley, v0.3 7B 

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

# 2D Hit Box Areas 
boxA2DArea = boxALength * boxAWidth
boxB2DArea = boxBLength * boxBWidth

# 3D Hit Box Area 
boxA3DArea = boxALength * boxAWidth * boxAHeight
boxB3DArea = boxBLength * boxBWidth * boxBHeight

# Input Hit Box Measurements
boxALength = int(input("Please enter the LENGTH of box A.\n")) 
boxAWidth = int(input("Please enter the WIDTH of box A.\n")) 
boxAHeight = int(input("Please enter the HEIGHT of box A.\n")) 

boxBLength = int(input("Please enter the LENGTH of box B.\n")) 
boxBWidth = int(input("Please enter the WIDTH of box B.\n")) 
boxBHeight = int(input("Please enter the HEIGHT of box B.\n")) 

