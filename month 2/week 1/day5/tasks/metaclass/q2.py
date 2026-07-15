class MyMeta(type):
    def __new__(cls, name, bases, namespace):

        namespace["created_by"]="Admin"

        return super().__new__(cls, name, bases, namespace)
    
class Student(metaclass=MyMeta):
    pass

print(Student.created_by)