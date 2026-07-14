class gh(type):
    def __new__(cls,nn,bb,ss):
        ss["created_by"]= "admin"
        return super().__new__(cls,nn,bb,ss)
class yo(metaclass=gh):
    pass

print(yo.created_by)       