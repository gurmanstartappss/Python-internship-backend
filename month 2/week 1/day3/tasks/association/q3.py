class Customer:
    def __init__(self, name):
        self.name = name

    def account(self, bank):
        print(self.name, "has account in", bank.name)

class Bank:
    def __init__(self, name):
        self.name = name


c1 = Customer("Gurman")
b1 = Bank("SBI")

c1.account(b1)