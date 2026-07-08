class Employee():
    def __init__(self,age):
        self.age=age
    
    @staticmethod
    def val(age):
        if age<18:
            return("minimum age is 18")
        else:
            return("welcome")


print(Employee.val(25))