# input original string. 
# Store the original string. 
# iterate through the string. 
    # if index is even, make it lower case. 
    # if index is odd, make it upper case. 
# output spongebobified string. 

def spongeBobify():
    originalString = input("Please enter the string to sPoNgEbObIfY.\n")
    newString = ""

    for i in range(0, len(originalString)): 
        if i % 2 == 0: # % divides and returns remainder.
            newString += originalString[i].lower()
        else: 
            newString += originalString[i].upper()
    print(f"\nYour original string is {originalString}\nThe string length is {len(originalString)}\n")
    print(f"\nYour new string is {newString}\nThe string length is {len(newString)}\n")
    
    
spongeBobify()

# function() can be called at any time, does not an 'object' to operate on. 
# .methods() MUST have an 'object' and require the . operator to execute. 

print() 
list = ["a", "c", "z", "f"]
print(list)
list.sort()
print(list)

# range(x, y)  START AT X, STOP Y - 1 