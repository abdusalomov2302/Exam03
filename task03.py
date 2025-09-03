
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def ovoz(self):
        print("Woof! Woof!")

d=Dog("Rex")
print(d.name)   
d.ovoz()        
