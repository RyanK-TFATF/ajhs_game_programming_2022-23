import time 

sum = 0 

lowerLimit = int(input("What is the lower limit?\n"))
upperLimit = int(input("What is the upper limit?\n"))

for n in range(lowerLimit, upperLimit + 1):
    print(f"n is {n}.")
    sum += (3 * n) * n
    print(f"The sum is {sum:,}.")
    time.sleep(0.10)

print(f"The final sum is: {sum:,}")

