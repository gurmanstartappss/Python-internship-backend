class Account():
    def __init__(self,roll):
        self.roll=roll
        
    def __eq__(self,other):
        return self.roll==other.roll
                                                                                            
x=(int(input("Enter account 1 balance")))
y=(int(input("Enter account 2 balance")))
a=Account(x)
b=Account(y)

print(a==b)