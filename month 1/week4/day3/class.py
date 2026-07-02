"""
inheritance and polymorphism

inheritance---one class inhert the properties and methods of another class
"""
#single inhertitance--single parent and child class(parent class instructor is default if no constructor is initialized in child class)

class Person: # parent class
    def __init__(self,name):
        self.name=name
        
    def eat(self):
        print("eating")
        
class Employee(Person): #child class
    def __init__(self):
        pass
    def work(self):
        print("employee is working")

    
obj1=Employee()
obj1.work()
obj1.eat()
print("--------------------------------")

#multilevel inheritance where 3 gen child class inherits methods from parent class which inherits methods from grandparent class so child has both class methods 
class Person: # grandparent class
    def __init__(self,name):
        self.name=name
        
    def eat(self):
        print("eating")
        
class Employee(Person): #parent class
    def __init__(self):
        pass
    def work(self):
        print("employee is working")
        obj1=Employee()
        
class Student(Employee): #child class
    def study(self):
        print("student is studying")

obj1=Student()
obj1.eat()
obj1.work()
obj1.study()
print("---------------------------------")

#multiple inheritance
class Person: # 1st parent class
    def __init__(self,name):
        self.name=name
        
    def eat(self):
        print("eating")
        
class Employee(): # 2nd parent class
    def __init__(self):
        pass
    def work(self):
        print("employee is working")
        obj1=Employee()
        
class Student(Employee,Person): #child class
    def study(self):
        print("student is studying")

obj1=Student()
obj1.eat()
obj1.work()
obj1.study()
print("----------------------------")
#hierarchical inheritance=single parent has multiple children so on methods of parent is called by multiple child classes
class Person: # single parent class
    def eat(self):
        print("eating")
        
class Employee(Person): # 1st child class
    def work(self):
        print("employee is working")
        obj1=Employee()
        
class Student(Person): # 2nd child class
    def study(self):
        print("student is studying")

obj1=Student()
obj2=Employee()
obj1.eat()
obj1.study()
obj2.eat()
obj2.work()
print("-----------------------")

# hierarchical inheritance=one parent has many children
class Person(): #parent class
    def work(self):         #work method 1
        print("eating")

class Employee(Person): #child class
    def work(self):                         #work method 2 this will override person work method so use super class for calling
        super().work()  # can also call parent constructor as well but should be mentioned after its own init only during both have same methods or multiple inheritance
        print("employee is working")

class Student(Person):
    def study(self):
        print("student is studying")

obj1 = Employee()
obj1.work()
print("-----------------------------------")

"""
super() used when 1 method overrides other, this method represents parent class and is used to call parent class's constructors (__init__),methods as well as attributes(self.name)
"""

# hybrid inheritance=when more then 1 inheritance is used 

class Person(): #parent class
    def work(self):         #work method 1
        print("eating")

class Employee(Person): #child class
    def work(self):                         #work method 2 this will override person work method so use super class for calling
        super().work()  # can also call parent constructor as well but should be mentioned after its own init only during both have same methods or multiple inheritance
        print("employee is working")

class Student(Person):
    def study(self):
        print("student is studying")

class Child(Employee, Student):
    def work():
        print("working")

obj1 = Employee()
obj1.work()
print("----------------------------------")


# mro-method resolution order is the order in which python searches for a method or attribute when its called on as object
# in this code in java error at run time 
# but in py it calls parent class method person first
class Person(): 
    def work(self):         
        print("eating")

class Employee(Person): 
    def work(self):
        super().work()                         
        print("employee is working")
class Manager(Person): 
    def work(self):                         
        print("manager is working")

class Student(Employee,Manager):
    def work(self):
        super().work()                        
        print("student is studying")

obj1 = Student()
obj1.work()