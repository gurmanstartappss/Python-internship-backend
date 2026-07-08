from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("car started")
        
class Bike(Vehicle):
    def start(self):
        print("bike started")
        
Car=Car()
Bike=Bike()

Bike.start()
Car.start()