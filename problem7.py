from abc import abstractmethod


class Payment:
    @abstractmethod
    def pay(self, amount):
        pass


class StripeAdapter:
    def pay(self, amount):
        print(f"Charging ${amount} with Stripe")


class PayPalAdapter:
    def pay(self, amount):
        print(f"Processing ${amount} with PayPal")


class LocalAdapter:
    def pay(self, amount):
        print(f"Handling ${amount} with LocalBankAPI")


def process_payment(gateway, amount):
    gateway.pay(amount)


stripe = StripeAdapter()
paypal = PayPalAdapter()
local = LocalAdapter()

process_payment(stripe, 100)
process_payment(paypal, 200)
process_payment(local, 300)
