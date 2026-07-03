class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("meow")
class Cow:
    def sound(self):
        print("moo")
        
animals=[Dog(),Cat(),Cow()]

for i in animals:
    i.sound()