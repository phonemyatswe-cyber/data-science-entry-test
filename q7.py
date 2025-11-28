
# Task 1
class Car:
    def __init__(self, make, model, year): #a class named Car was initialized with __init__ method with specified attributes
        self.make = make
        self.model = model
        self.year = year


    def describe_car(self): # this method is to print information about the car as Year Make Model
        print(f"{self.year} {self.make} {self.model}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
car1 = Car("Toyota", "Corolla", 2020) # car1 instance of the Car class was created
car1.describe_car() #Called the describe_car() method to print. Expected output 2020 Toyota Corolla