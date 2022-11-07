# Collection  Examples, Ryan Kelley, 11/07/22, 10:26AM, v0.0

# List Characteristics 
# ORDERED -- Items have defined order, can be indexed.  Location in the list is the INDEX.  First item is index 0. 
# CHANGEABLE -- Items can be changed, added, or removed.  Items added are ALWAYS added to the end of the list. 
# DUPLICATES -- Items can be duplicated within a list.  

# List Examples -- Integer, Float, and String Examples v0.1a

testScores = [15, 25, 99, 73, 25] # Integers
gradePointAvg = [1.99, 2.5, 3.75, 4.0, 0.99] # Floats
courseOptions = ["Math", "Science", "Reading", "Gym"]

# Print List Contents v0.1b
print(testScores)
print(gradePointAvg)
print(courseOptions + "\n")

# List Length -- Determine number of items in a list. v0.2 
print("Determining the length of each list:")
print(f"The testScores list contains {len(testScores)} items.\n")
print(f"The gradePointAvg list contains {len(gradePointAvg)} items.\n")
print(f"The courseOptions list contains {len(courseOptions)} items.\n")

# Accessing List Items -- v0.3a
print("Accessing the first item in each list:")
print(testScores[0]) # Print the first item in the list. 
print(gradePointAvg[0]) # Print the first item in the list. 
print(courseOptions[0] + "\n") # Print the first item in the list. 

# PAUSE VIDEO -- Print the Third List Item from Each List -- v0.3b 
print("Accessing the third item in each list:\n")
print(testScores[2]) # Print the first item in the list. 
print(gradePointAvg[2]) # Print the first item in the list. 
print(courseOptions[2] + "\n") # Print the first item in the list. 

# Python ONLY -- Negative Indexing -- v0.3c 
print("Accessing the last item in each list:\n")
print(testScores[-1]) # Print the last item in the list. 
print(gradePointAvg[-1]) # Print the last item in the list. 
print(courseOptions[-1] + "\n") # Print the last item in the list. 

# PAUSE VIDEO -- Print the Third From Last List Item from Each List -- v0.3d
print("Accessing the third from last item in each list:\n")
print(testScores[-3]) # Print the last item in the list. 
print(gradePointAvg[-3]) # Print the last item in the list. 
print(courseOptions[-3] + "\n") # Print the last item in the list. 

# Accessing List Ranges -- v0.3e 

# Changing List Items -- v0.4a 
testScores[0] = 75
gradePointAvg[0] = 2.5
courseOptions[0] = "Algebra 1"
print("Accessing the updated first item in each list:\n")
print(testScores[0]) # Print the first item in the list. 
print(gradePointAvg[0]) # Print the first item in the list. 
print(courseOptions[0] + "\n") # Print the first item in the list. 

# PAUSE Video -- Changing List Items -- v0.4b
testScores[1] = 35
gradePointAvg[1] = 1.5
courseOptions[1] = "Physics"
print("Accessing the updated second item in each list:")
print(testScores[1]) # Print the first item in the list. 
print(gradePointAvg[1]) # Print the first item in the list. 
print(courseOptions[1]) # Print the first item in the list. 


# Add List Items, Always Adds to End of List -- v0.4c 
testScores.append(100)
gradePointAvg.append(0.0)
courseOptions.append("Cooking")
print(testScores)
print(gradePointAvg)
print(courseOptions)

