# import os 

# dirName = "TestDirectory"
# os.mkdir(dirName)

# import math
# pi = math.pi 
# radius = (float(input("Enter a radius for a circle.\n")))
# area = pi * radius ** 2
# print(area)

# from modulename import functionname 
# from random import randint 
# import sys 

import os 

writeFile = open('log.txt', 'a')

writeFile = open('log.txt', 'w')

toLog = input("What do you want to write to the log?")

writeFile.close()