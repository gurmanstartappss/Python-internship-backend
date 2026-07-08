class Employee():
    classv="company"
    @classmethod
    def update(cls,new):
        cls.classv=new
    @classmethod
    def get(cls):
        return cls.classv
Employee.update("startappss")
print(Employee.get())