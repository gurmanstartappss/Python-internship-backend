from abc import abstractmethod,ABC

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"{amount} paid using UPI")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"{amount} paid using CARD")
class PayPalPayment(Payment):
    def pay(self,amount):
        print(f"{amount} paid using PAYPAL")
        
class PaymentFactory:

    @staticmethod
    def create_payment(payment_type):

        if payment_type == "upi":
            return UPIPayment()

        if payment_type == "card":
            return CardPayment()

        if payment_type == "paypal":
            return PayPalPayment()
        
payment = PaymentFactory.create_payment('upi')
payment.pay(1000)