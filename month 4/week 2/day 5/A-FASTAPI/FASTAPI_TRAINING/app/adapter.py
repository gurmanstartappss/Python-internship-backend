class PaymentProcessor:
    def pay(self, amount):
        pass


class StripPayment:
    def make_payment(self, amount):
        print(f"Payment of {amount} made using Stripe")


class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_payment):
        self.stripe_payment = stripe_payment

    def pay(self, amount):
        self.stripe_payment.make_payment(amount)


stripe = StripPayment()
payment = StripeAdapter(stripe)

payment.pay(500)