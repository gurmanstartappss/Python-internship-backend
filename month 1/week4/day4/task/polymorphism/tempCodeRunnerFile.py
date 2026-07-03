class CreditCard:
    def pay(self):
        print("Payment made using Credit Card")

class UPI:
    def pay(self):
        print("Payment made using UPI")

class Wallet:
    def pay(self):
        print("Payment made using Wallet")

def make_payment(payment):
    payment.pay()
    

x = CreditCard()
y = UPI()
z = Wallet()


make_payment(x)
make_payment(z)
make_payment(y)