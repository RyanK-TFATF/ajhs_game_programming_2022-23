# Monsters, Ryan Kelley, v0.0 


class Monster: 
    def __init__(self, prop1, prop2, prop3): 
        self.prop1 = prop1
        self.prop2 = prop2 
        self.prop3 = prop3 
        self.experience = 50000 

    def __str__(self): 
        return f"Monster Name: {self.prop1}\nHit Points: {self.prop2}\nLevel: {self.prop3}\nXP Value: {self.experience}\n"
    
    
    
myMonster = Monster("Fire Dragon", 2500, 25)
print(myMonster)
