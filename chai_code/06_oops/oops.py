class Car:
    total_cars = 0  # Class variable to keep track of the total number of cars

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1  # Increment the total number of cars when a new car is created

    def start_engine(self):
        pass  # Placeholder for starting the engine

    def get_car_info(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol and Diesel"  # Default fuel type for a generic car

my_car = Car(brand="Toyota", model="Corolla")

print(my_car.get_car_info())
print(f"Fuel type: {my_car.fuel_type()}")

my_car.start_engine()

my_new_car = Car(brand="Honda", model="Civic")
print(my_new_car.get_car_info())


# inheritance example
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model) # Call the constructor of the parent class
        self.battery_capacity = battery_capacity

    def get_car_info(self):
        return f"{self.brand} {self.model} with battery capacity of {self.battery_capacity} kWh"

    def fuel_type(self):
        return "Electric"  # Override the fuel type for electric cars


my_electric_car = ElectricCar(brand="Tesla", model="Model 3", battery_capacity=75)
print(my_electric_car.get_car_info())
print(f"Fuel type: {my_electric_car.fuel_type()}")

print(f"Total cars created: {Car.total_cars}")

# check isinstance example
print(isinstance(my_car, Car))  # True

# encapsulation example
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute by convention __

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance


my_account = BankAccount(account_number="123456789", balance=1000)
my_account.deposit(500)
print(f"Initial balance: ${my_account.get_balance()}")


# polymorphism example
class Animal:
    def speak(self):
        pass  # Placeholder for animal sound


# Static method example
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero."


# @property decorator example
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Protected attribute by convention _

    @property # getter for radius
    def radius(self):
        return self._radius

    @radius.setter # setter for radius
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            print("Radius must be positive.")

    @property
    def area(self):
        import math
        return math.pi * (self._radius ** 2)


new_circle = Circle(radius=5)
print(f"Circle radius: {new_circle.radius}")
print(f"Circle area: {new_circle.area}")


# multiple inheritance example
class Vehicle:
    def start(self):
        print("Vehicle started.")

class Engine:
    def start(self):
        print("Engine started.")

class Car(Vehicle, Engine):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_car_info(self):
        return f"{self.brand} {self.model}"

my_car = Car(brand="Toyota", model="Camry")
my_car.start()  # Calls the start method from the Vehicle class
my_car.get_car_info()