#create boject for parent in abstract acatn
#i need to have tranction every child class



from abc import ABC,abstractmethod

class Phonepay(ABC):

    def senderinfo(self):
        print("you can enter their mobil number or scanner")
    def amount(self):
        print("you can enter amount")
    def pin(self):
        print("enter the pin")

    @abstractmethod
    def transaction(self):
        pass

class HDFC(Phonepay):
    def transaction(self):
        print("payment using HDFC")
class SBI(Phonepay):
    def transaction(self):
        print("payment using SBI")
class UNION(Phonepay):
    def transaction(self):
        print("payment using UNION")
class ICIC(Phonepay):
    def transaction(self):
        print("payment using ICIC")
class CANARA(Phonepay):
    def transaction(self):
        print("payment using CANARA")



zaib=HDFC()
zaib.senderinfo()
zaib.amount
zaib.pin()
zaib.transaction()




sajid=UNION()
sajid.senderinfo()
sajid.amount
sajid.pin()
sajid.transaction()





class regester:
    def __init__(self,name, email,phone,password):
        self.name=name
        self.email=email
        self.password=password
        self.password=password
    def register(self):

        if all ([self.name,self.email,self.phone,self.password]):
            return"registraction successful"
        else:
            return"all feild are required for reistration"
user=regester("ZAIB,ZAIBEF","9876890","YFYUF2312@11")

user.register()