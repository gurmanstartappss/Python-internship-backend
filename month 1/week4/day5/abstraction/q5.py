from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

    def move(self):
        print("Dog walks")

class Bird(Animal):
    def sound(self):
        print("Bird chirps")

    def move(self):
        print("Bird flies")

d = Dog()
b = Bird()

d.sound()
d.move()

b.sound()
b.move()