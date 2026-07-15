class gh(type):
    def __new__(cls,nn,bb,ss):
        count=0
        for key in ss:
            if not key.startswith("__") :
                count+=1
        ss["attribute_count"]=count
        
        return super().__new__(cls,nn,bb,ss)
class yo(metaclass=gh):
    def show(name,class):
        return 

print(yo.attribute_count)       