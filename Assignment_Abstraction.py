from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $3000.00 limit!".format(amount))

class CashPayment(car):
    def payment(self, amount):
        print("Your purchase amount of {} via cold hard cash has been graciously accepted!".format(amount))

class BitCoinPayment(car):
    def payment(self, amount):
        print("Im sorry we cannot approve this transaction of {} as we do not accept BitCoin.".format(amount))

Debit = DebitCardPayment()
Debit.paySlip("$4000")
Debit.payment("$4000")

Cash = CashPayment()
Cash.paySlip("30000")
Cash.payment("30000")

BitCoin = BitCoinPayment()
BitCoin.paySlip("1.5 million")
BitCoin.payment("1.5 million")

