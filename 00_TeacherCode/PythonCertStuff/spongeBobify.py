def spongeBobify():
    originalString = input("Please enter a string to sPoNgEbObIfY!\n")
    newString = ""    

    for i in range(0, len(originalString)):        
        if i % 2 == 0: 
            newString += originalString[i].lower()
        else:
            newString += originalString[i].upper()
    print(f"\nYour original string is\n{originalString}\nThe string length is {len(originalString)}\n")    
    print(f"\nYour sPoNgEbObIfIeD string is\n{newString}\nThe string length is {len(newString)}\n")
    
    

spongeBobify()
