import logging 

logging.basicConfig(
    filename="Log.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s - %(levelname)s"
    
)
class MyMeta(type):
    def __new__(mcls,name,bases,namespace):
        logging.info("%s class created ",name)
        logging.error("%s class created ",name)
        print(name,"class created ")
        return super().__new__(mcls,name,bases,namespace)
    

class Student(metaclass=MyMeta):
    pass
class Employee(metaclass=MyMeta):
    pass
