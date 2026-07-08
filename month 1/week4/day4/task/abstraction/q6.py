from abc import ABC,abstractmethod
class Vehicle(ABC):
    def display(self):
        print("normal method")
        
    @abstractmethod
    def sound(self):
        return "vehicle"
    
class Bike(Vehicle):
    def sound(self):
        print("bike honk")
class Car(Vehicle):
    def sound(self):
        print("Car honk")
        
car=Car()
bike=Bike()
bike.display()
bike.sound()
car.display()
car.sound()
