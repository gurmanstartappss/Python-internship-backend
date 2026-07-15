class Age():
    def __get__(self,instance,owner):
        return instance.__dict__._get("age")
    def __set__(self,instance,value):
        if value<18:
            raise ValueError("age must be greater than 18")
        instance.__dict__["age"]