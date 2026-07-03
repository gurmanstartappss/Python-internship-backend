class Animal:
    def walk(self):
        print("animal is walking ")
class Dog(Animal):
    def bark(self):
        print("dog is barking ")
class Cat(Animal):
    def meow(self):
        print("cat is meowing ")
class Lion(Animal):
    def roar(self):
        print("lion is roaring ")
x=Dog()
y=Cat()
z=Lion()
x.bark()
x.walk()
y.meow()
y.walk()
z.roar()
z.walk()