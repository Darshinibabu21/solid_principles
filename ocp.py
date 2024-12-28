from abc import ABC , abstractmethod

class payment(ABC):
    @abstractmethod
    def process(self,amount):
        pass

class credit(payment):
    def process(self,amount):
        print(f"credit card amount is {amount}")

class paypal(payment):
     def process(self,amount):
        print(f"paypal amount is {amount}")

class processor:
    def __init__(self,payment_method:payment):
        self.payment_method=payment_method

    def process(self,amount):
        self.payment_method.process(amount)

pay=processor(paypal())
pay.process(100)
        
 