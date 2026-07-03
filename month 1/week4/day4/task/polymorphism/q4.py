class Animal():
    def walk(self):
        print("animal is walking ")
class Dog(Animal): 
    def walk(self):
        print("Dog is walking ")
class Cat(Animal):
    def walk(self):
        print("Cat is walking ")
        

x = Animal()
y = Dog()
z = Cat()

x.walk()
y.walk()
z.walk()