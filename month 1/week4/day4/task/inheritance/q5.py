class BankAccount():
    def balance(self):
        print("Account balance ")
class CurrentAccount(BankAccount):
    def current(self):
        print("total balance in current")
class SavingsAccount(BankAccount):
    def savings(self):
        print("total balance in savings")
x=CurrentAccount()
y=SavingsAccount()

x.current()
x.balance()
y.savings()
y.balance()