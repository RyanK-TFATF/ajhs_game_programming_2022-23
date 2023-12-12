# Classes and Objects Practice Code, Ryan Kelley, v0.0 
import testmodule
testmodule.testFunction()

class Person: 
    def __init__(self, age, height, weight, name):
        self.age = age
        self.height = height
        self.weight = weight
        self.name = name

    def __str__(self):
        return f"{self.name} is {self.age} years old, weighs {self.weight} pounds and is {self.height} tall.\n"

    


examplePerson0 = Person(25, "6'2\"", 250, "Bob")
examplePerson1 = Person(35, "7'2\"", 150, "Dennis")
examplePerson2 = Person(45, "5'2\"", 350, "Mud")

if examplePerson0.weight > examplePerson1.weight: 
    print(f"{examplePerson0.name} weighs more than {examplePerson1.name}.")
else:
    print(f"{examplePerson1.name} weighs more than {examplePerson0.name}.")

people = [examplePerson0, examplePerson1, examplePerson2]
for i in people: 
    print(i)

# print(examplePerson.age)
# print(examplePerson.height)
# print(examplePerson.weight)
# print(examplePerson.name)
# print(examplePerson)

