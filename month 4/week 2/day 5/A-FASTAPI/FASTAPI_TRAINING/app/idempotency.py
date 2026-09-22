class PaymentService:

    def __init__(self):
        self.processes_payments = {}

    def process_payment(self, idempotency_key, amount):

        # Check if payment was already processed
        if idempotency_key in self.processes_payments:
            print("Duplicate request detected")
            return self.processes_payments[idempotency_key]

        # Process new payment
        print("Processing payment...........")

        result = {
            "status": "success",
            "amount": amount,
            "transaction_id": "1234567890"
        }

        # Store payment result
        self.processes_payments[idempotency_key] = result

        return result


# Create PaymentService object
paymentService = PaymentService()


# First payment request
result1 = paymentService.process_payment("ORDER123", 500)
print(result1)


# Same request again
result2 = paymentService.process_payment("ORDER123", 500)
print(result2)


# Another payment with a different idempotency key
result3 = paymentService.process_payment("ORDER456", 1000)
print(result3)


