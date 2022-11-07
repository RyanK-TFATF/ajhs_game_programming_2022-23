# Calc. Hit Boxes, ryan kelley, v0.1 11-07-22 13:57 

# Hit Box Type 
boxType = 0 # 1 = 2D Box, 2 = 3D Box 

# Box A
boxALength = 0 
boxAWidth = 0 
boxAHeight = 0 

# Box B
boxBLength = 0 
boxBWidth = 0 
boxBHeight = 0 

# Box A Area Calcs. 
boxA2D = boxAWidth * boxALength
boxA3D = boxAWidth * boxALength * boxAHeight

# Box B Area Calcs. 
boxB2D = boxBWidth * boxBLength
boxB3D = boxBWidth * boxBLength * boxBHeight

# Determine Hit Box Type 
boxType = int(input("Please select a hit box type.  1 = 2D box, 2 = 3D box.\n"))

if boxType == 1:
    print("You have chosen a 2D hit box.\n")
elif boxType == 2:
    print("You have chosen a 3D hit box.\n")
else:
    print("Invalid box selection, please restart the program.\n")

# Box A Measurements 
boxALength = int(input("Please enter an integer value for Box A Length.\n"))


# Box B Measurements 


