# Classes and Objects, Ryan Kelley, v0.0 

class Person:  # Class names should be PascalCase
    def __init__(self, age, height, hairColor, name, weight, birthday):
        # The self keyword refers to the specific object you are dealing with. 
        self.age = age
        self.height = height
        self.hairColor = hairColor
        self.name = name
        self.weight = weight
        self.birthday = birthday

    # __str__ Method Format
    def __str__(self): 
        return f"{self.name} is {self.age} years old.\nThey have {self.hairColor} hair and weigh {self.weight} pounds.\nThey were born on {self.birthday} and stands {self.height} tall.\n"
    

    # Functions In A Class 
    def tooOld(self): 
        print("Hello, this function will determine if you are too old to ride.\n")
        print("If you are older than 25 years, you cannot ride this ride.\n")
        if self.age > 25:
            print("You are too old, go find a different ride.\n")
        else: 
            print("Welcome aboard!\n")


# A class is a 'blueprint' to make an object. 

examplePerson = Person(36, "6'2\"", "black", "Bob", 500, "April 01")
examplePerson1 = Person(25, "5'3\"", "blonde", "Jennifer", 150, "July 01")

class Animals: 
    def __init__(self, age, height, hairColor, name, weight, birthday):
        # The self keyword refers to the specific object you are dealing with. 
        self.age = age
        self.height = height
        self.hairColor = hairColor
        self.name = name
        self.weight = weight
        self.birthday = birthday

animal1 = Animals(25, "5'3\"", "blonde", "Jennifer", 150, "July 01")
examplePerson.tooOld() 
# anmimal1.tooOld() 
# print(examplePerson)

# # Changing Properties After Creating Object
# print(examplePerson1.weight)
# examplePerson1.weight = 200 
# print(examplePerson1.weight)

# Deleting Properites from Objects 
# print(examplePerson.name)
# del examplePerson.name 
# print(examplePerson.name)
# del COMPLETELY removes the property.  

# Deleting Whole Objects 
print(examplePerson1)
del examplePerson1
# print(examplePerson1)
# Delete objects that are no longer needed to free up memory. 

examplePerson.weakness = "Krpytonite"
print(examplePerson.weakness)







