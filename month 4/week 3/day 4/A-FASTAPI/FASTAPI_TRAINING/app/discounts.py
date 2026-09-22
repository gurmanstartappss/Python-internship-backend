from abc import abstractmethod,ABC

class DiscountStrategy(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
class NoDiscount(DiscountStrategy):
    def pay(self,amount):
        return amount*0.30
    
class FestivalDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        return amount * 0.20   

class ShoppingCart(DiscountStrategy):
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def calculate_final(self, amount):
        discount = self.discount_strategy.calculate_discount(amount)
        return amount - discount



payment = ShoppingCart(FestivalDiscount())

print(payment.calculate_final())