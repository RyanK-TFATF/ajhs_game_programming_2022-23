# Collection  Examples, Ryan Kelley, 11/07/22, 10:26AM, v0.0

# List Characteristics 
# ORDERED -- Items have defined order, can be indexed.  Location in the list is the INDEX.  First item is index 0. 
# CHANGEABLE -- Items can be changed, added, or removed.  Items added are ALWAYS added to the end of the list. 
# DUPLICATES -- Items can be duplicated within a list.  

# List Examples -- Integer, Float, and String Examples v0.1

testScores = [15, 25, 99, 73, 25] # Integers
gradePointAvg = [1.99, 2.5, 3.75, 4.0, 0.99] # Floats
courseOptions = ["Math", "Science", "Reading", "Gym"]

# List Length -- Determine number of items in a list. v0.2 
print("Determining the length of each list:\n")
print(f"The testScores list contains {len(testScores)} items.\n")
print(f"The gradePointAvg list contains {len(gradePointAvg)} items.\n")
print(f"The courseOptions list contains {len(courseOptions)} items.\n")

# Accessing List Items -- v0.3a
print("Accessing the first item in each list:\n")
print(testScores[0]) # Print the first item in the list. 
print(gradePointAvg[0]) # Print the first item in the list. 
print(courseOptions[0]) # Print the first item in the list. 

# PAUSE VIDEO -- Print the Third List Item from Each List -- v0.3b 
print("Accessing the third item in each list:\n")
print(testScores[2]) # Print the first item in the list. 
print(gradePointAvg[2]) # Print the first item in the list. 
print(courseOptions[2]) # Print the first item in the list. 

# Python ONLY -- Negative Indexing -- v0.3c 
print("Accessing the last item in each list:\n")
print(testScores[-1]) # Print the last item in the list. 
print(gradePointAvg[-1]) # Print the last item in the list. 
print(courseOptions[-1]) # Print the last item in the list. 

# PAUSE VIDEO -- Print the Third From Last List Item from Each List -- v0.3d
print("Accessing the third from last item in each list:\n")
print(testScores[-3]) # Print the last item in the list. 
print(gradePointAvg[-3]) # Print the last item in the list. 
print(courseOptions[-3]) # Print the last item in the list. 

# 