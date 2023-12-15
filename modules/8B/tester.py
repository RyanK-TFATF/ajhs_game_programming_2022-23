import perfmon  
start = perfmon.execStart() 
print(start)




roll1 = dice.display(1, 6)
roll2 = dice.display(1, 6)


x = 0
while x < 100: 
    if dice.isExploding(roll1, 6): 
        print(roll1)
        print("This roll exploded!\n")
        roll1 += dice.roll(1, 6)
        print(roll1)
    x += 2 

stop = perfmon.execStop() 

print(perfmon.execTime(start, stop))



