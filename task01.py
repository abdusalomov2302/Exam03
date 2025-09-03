

class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year


    def get_info(self):
        return f"brand: {self.brand},model: {self.model},year: {self.year}"

car1=Car('BMW','X5',2024)
car2=Car("Mercedes",'M7',2023)
car3=Car("Cobolt",'A4',2020)

print(car1.get_info())
print(car2.get_info())
print(car3.get_info())