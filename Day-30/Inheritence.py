class whatsappV1:
    def __init__(self,name):
        self.name=name
        print(f"Welcome to the whatsapp-v1{self.name}!")
    def messaging(self):
        print("You can send messages")

class whatsappV2(whatsappV1):
    def __int__(self,name):
        self.name=name
        print(f"Welcome to the whatsapp-v2{self.name}!")
    def calls(self):
        print("You can Audio and Video Calls")





zaib= whatsappV1("zaib")
zaib.messaging()

sajid=whatsappV2("sajid")
sajid.messaging()
sajid.calls()