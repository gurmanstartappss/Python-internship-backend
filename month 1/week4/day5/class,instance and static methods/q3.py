class Calculator():
    def __init__(self,a):
        self.a=a
    @staticmethod
    def add(a):
        return a**2
    
print(Calculator.add(22))