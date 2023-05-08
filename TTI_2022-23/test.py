import os 
wF = open('sample.txt', 'w')
wF.write("Yolo")
wF.close()
wF = open('sample.txt', 'r')
print(wF)
