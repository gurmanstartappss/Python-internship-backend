class MyMeta(type):
    def __new__(cls,name,bases,namespace):
        new_namespace={}
        for key,value in namespace.items():
            if not key.startswith("__"):
                new_namespace[key.upper()]=value
            else:
                new_namespace[key]=value
        return super().__new__(cls,name,bases,new_namespace)
    
class Student(metaclass=MyMeta):
    name="gurman"
    age=23
    
x=Student()
print(x.NAME)
print(x.AGE)