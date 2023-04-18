print("Try/Except/Else/Finally Example\n")
eF = open("example.txt", "x")
try: 
    eF = open("example.txt", "x")
    try: # Run the code in this block always. 
        eF.write("Writing to the file.\n")
    except: # If errors, run this block.        
        print("This file is read only!\n")
    finally: # If no errors, run this block last.
        eF.close()
except: 
    print("Error trying to open the file.\n")

