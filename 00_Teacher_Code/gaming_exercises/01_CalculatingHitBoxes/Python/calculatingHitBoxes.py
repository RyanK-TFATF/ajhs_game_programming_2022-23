# Variable Declarataions       
hitBoxType = 0 # 1 = 2D hit box, 2 = 3D hit box

# Hit Box A Measurements 
hitBoxALength = 0
hitBoxAWidth = 0 
hitBoxAHeight = 0
            
# Hit Box B Measurements 
hitBoxBLength = 0
hitBoxBWidth = 0 
hitBoxBHeight = 0

# 2D Hit Box Calculations
area2DHitBoxA = hitBoxALength * hitBoxAWidth
area2DHitBoxB = hitBoxBLength * hitBoxBWidth
                    
# 3D Hit Box Calculations
area3DHitBoxA = hitBoxALength * hitBoxAWidth * hitBoxAHeight
area3DHitBoxB = hitBoxBLength * hitBoxBWidth * hitBoxBHeight