class Person:
    def init(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"{self.name}, {self.age} years old"


class Employee(Person):
    def init(self, name, age, company):
       
        super().init(name, age)
        self.company = company
    
    def get_info(self):
        
        b= super().get_info()
        return f"{b}, works at {self.company}"

e=Employee("Azimbek", 25, "Google")
print(e.get_info())