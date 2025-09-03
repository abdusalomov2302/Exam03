class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def introduce(self):
        return f"My name is {self.name},Im old {self.age},Im {self.course} course"
        
s1=Student("Azimbek",20,3)
s2=Student("Sevara",100,3)
    
print(s1.introduce())
print(s2.introduce())

        
    