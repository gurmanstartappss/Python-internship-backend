# Formatter:
# Controls how log messages appear.
# It defines the layout of log messages by adding information
# such as date/time, log level, filename, and message.

format = "%(asctime)s - %(levelname)s - %(filename)s - %(message)s"

# %(asctime)s   = Date and time
# %(levelname)s = Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# %(filename)s  = Name of the file where the log occurred
# %(message)s   = Actual log message
# %(lineno)d   = Line number

# %(funcName)s  = Function name



import logging

logging.basicConfig(
    filename="demo.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)d - %(funcName)s"
)

logging.debug("Debugging application")
logging.info("")
logging.warning("insuffient space")
logging.error("program error")
logging.critical("server crashed")

def demo():
    try:
        with open("students.txt", "r") as file:
            print(file.read())

    except:
        logging.error("file not found")
        
        
#handlers:a handler specifies the destination of the log messages.diff handlers can send log to diff locations 
# 1. StreamHandler    : Sends logs to console/terminal
# 2. FileHandler      : Sends logs to a file
# 3. RotatingFileHandler : Sends logs to a file and creates a new file when size limit is reached
# 4. SMTPHandler      : Sends logs through email

# 1)streamhandler

import logging

logger = logging.getLogger("console_logger")
logger.setLevel(logging.WARNING)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

logger.warning("Console warning")

# 2) FileHandler

import logging

logger = logging.getLogger("Employee")
logger.setLevel(logging.INFO)

# Handler → WHERE logs go
file_handler = logging.FileHandler("employee.log")

# Formatter → HOW logs look
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s - "
    "%(filename)s - %(lineno)d - %(funcName)s"
)

# Attach formatter to handler
file_handler.setFormatter(formatter)

# Attach handler to logger
logger.addHandler(file_handler)


def Employee(emp):
    if emp == 3:
        logger.error("Employee id already exists.")
    else:
        logger.info("Employee created successfully")


Employee(3)

#metaclass=meta class is a class that creates other classes just as objects are created from classes, classes themselves are cre ated from meta classes 
# # # when we created a class(then type () gets executed and creates a class )
# if we create a class Employee():
# internally:-
"""type("class name"(parent class),{"show":lambda self:print("hello employee")})"""#methods and attributes
class MyMeta(type):# type=default metaclass in Python.
    def __new__(cls,name,bases,attrs):
        print(f"Creating Class:{name}")
        attrs["display"]=lambda self:print("welcome")
        return super().__new__(cls,name,bases,attrs)

class Student(metaclass=MyMeta):
    pass
x=Student()
x.display()

class Hahha(metaclass=MyMeta):
    pass
class HEHHE(metaclass=MyMeta):
    pass

# Descriptor(__get__ and __set__) use magic method as attributes 
# # it is an object that controls how another objects are accessed, modified or deleted using magic method s like __get__() and __set__()
# use case=use for data validation,orm fields validation,property

class Age:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Age should be >= 0")

        instance._age = value


class Student:
    age = Age()


obj = Student()
obj.age = 30
print(obj.age)

# 3rd concept is __slots__=used for limiting the attributes an object can have, reducing memory usage and preventing accidental
class Student:
    __slots__=["name","age"]
student=Student()
student.age=40
student.name="gurman"
# student.city="gurman" # student has no attributes named city
# print(student.city)
print(student.age)
print(student.name)

# saves memory, faster attribute access, preventing unnessasary attribute creation