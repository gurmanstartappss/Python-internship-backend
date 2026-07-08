# polymorphism one name many forms
# operation behaves differently depending on the object that uses it
class Dog:
    def sound(self):
        print("bark")

class cat:
    def sound(self):
        print("meow")        

class cow:
    def sound(self):
        print("moo")        
        
x=Dog()
y=cat()
z=cow()
x.sound()
y.sound()
z.sound()

"""
to achieve polymorphism (now pythjon is a runtime polymorphism whereas java and c++ support compile time polymorphism )
compile time polymorphism = does support (method overloading-same name diff para meters)
runtime polymorphism=does support (method overriding=same name with same parameters)(achieved in inheritance)
"""


class Animal:
    def add(self,*args):
        total=0
        for i in args:
            total+=i
        print(total)

obj=Animal()
obj.add(3,4,5)
obj.add(3,4,5,76,3,3,7,9)

# built in polymorphism

max(1,3,5,6,8)    
sum([1,3,5,6,8])  
sum((1,3,5,6,8))  
sum({1,3,5,6,8})             


# duck typing focus on only behavoiur Duck typing means Focuses on whether If an object has the required methods or attributes

class Dog:
    def speak(self):
        print("Bark")
        
class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())
# abstraction
# process of hiding implementation details and showing only the essential features

from abc import ABC,abstractmethod  #abstract base class
#abstract base method=method that must be implemented by child classes
#abstract class=abstract class is a blueprint for other class,we cant create its object directly but child classes can inherit its methods 
# (cant create a object with this method)
#ABC=provided by python to create abstract classes it defines comman rules that all classes must  follow 
#abstractmethod=its a decorator that declares a method which every child class must implement A subclass be create
class demo(ABC):
    @abstractmethod# this hides the implementation details 
    def say (self):
        print("hello")
        
obj=demo()# this does not get created so we cant access the methods in the abstract class 
