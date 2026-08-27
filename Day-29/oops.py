#flipkart
class Flipkart:
    products = {'Shirt':200,"Bags":90,"pants":195}
    discount=30
    @classmethod
    def display(cls):
        print(cls.products)


    def userinfo(self,name,number,address):
        self.name=name
        self.number=number
        self.address=address


        print(f"Hello {self.name},Welcome to the flipkart")


    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount} % discpunt is going on, grab the products..")




zaib=Flipkart()
zaib.userinfo("zaib",98767890,"hyd")
zaib.displaydiscount()
zaib.display()



sajid=Flipkart()
sajid.userinfo("sajid",9877890987,"pak")
sajid.displaydiscount()
sajid.display()


#instat,static and class methods -3 methods
#2 class ,insta attribute -2 attribute



#https://chatgpt.com/share/6a8bcac2-418c-83ee-9ac9-a49181bb7a94