class CreditcardPayment:
    def pay(self,amount):
        return f"paid{amount} using credit card "
class Paypalpayment:
    def pay(self,amount):
        return f"paid{amount} using paypal "
class Debitcard:
    def pay(Self,amount):
        return f"paid {amount}using debit card"
def process_payment(ccp,amount):
    print(ccp.pay(amount))
cc=CreditcardPayment()
process_payment(cc,200)
pp=Paypalpayment()
process_payment(pp,300)
dp=Debitcard()
process_payment(dp,400)


    