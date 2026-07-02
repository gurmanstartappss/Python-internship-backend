class Vehicle:
    def start(self):
        print("Engine started ")
        
class Car(Vehicle):
    def go(self):
        print("Car is driving ")
class Bike(Vehicle):
    def zoom(self):
        print("Bike is riding ")
class Truck(Vehicle):
    def thruu(self):
        print("Car is loading ")

car=Car()
bike=Bike()
truck=Truck()

car.start()
bike.start()
truck.start()
car.go()
bike.zoom()
truck.thruu()
