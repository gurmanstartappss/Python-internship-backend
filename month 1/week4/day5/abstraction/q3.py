from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Payment through UPI")

class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card")

class NetBanking(Payment):
    def pay(self):
        print("Payment through Net Banking")

u = UPI()
c = CreditCard()
n = NetBanking()

u.pay()
c.pay()
n.pay()