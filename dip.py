from abc import ABC ,abstractmethod

class mmessage(ABC):
    def send(self,message):
        pass

class sms(mmessage):
    def send(self,message):
        print(f"sms is :{message}")

class email(mmessage):
    def send(self,message):
        print(f"email is {message}")

class notification():
    def __init__(self,sender:mmessage):
        self.sender=sender
    def notify(self,message):
        self.sender.send(message)

e=notification(email())
e.notify("hello")

d=notification(sms())
d.notify("world!")

