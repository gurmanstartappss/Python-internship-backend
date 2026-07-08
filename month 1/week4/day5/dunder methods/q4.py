class Account():
    def __init__(self,balance):
        self.balance=balance
        
    def __add__(self,other):
        return self.balance+other.balance
                                                                                            
x=(int(input("Enter account 1 balance")))
y=(int(input("Enter account 2 balance")))
a=Account(x)
b=Account(y)

print(a+b)