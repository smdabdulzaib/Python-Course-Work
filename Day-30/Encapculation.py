
#also called exmaple of encapculation
class Instagram:
    def __init__(self,name,password):
        self.name=name#public
        self.__password=password  #__private
        self._posts=[]   #_protected


    def getpassword(self):
        return self.__password


    @property
    def accesspost(self):
        return self._posts


    def display(self):  #acees inside claass 
        print(self.name,self.__password,self._posts)

zaib=Instagram("zaib","zaib@1213")
zaib.display()     #for calling inside class we us new or create method caleed Display

print(zaib.name)#public                              # accessed directly
print(zaib.getpassword()) #private                   #we use method to access private caleed getpassword
print(zaib.accesspost) #protected                    #we use @property  to access protected  caleed accesspost







#also called exmaple of encapculation
class Instagram:
    def __init__(self,name,password):
        self.name=name#public
        self.__password=password  #__private
        self._posts=[]   #_protected


    def getpassword(self):
        return self.__password


    def setpassword(self,newpassword):
        self.__password=newpassword#edit password

    @property
    def accesspost(self):
        return self._posts
    @accesspost.setter
    def accesspost(self,newpost):#edit new posts
        self._posts.append(newpost)
    




    def display(self):  #acees inside claass 
        print(self.name,self.__password,self._posts)

zaib=Instagram("zaib","zaib@1213")
zaib.display()     #for calling inside class we us new or create method caleed Display

print(zaib.name)#public                              # accessed directly
print(zaib.getpassword()) #private                   #we use method to access private caleed getpassword
print(zaib.accesspost) #protected                    #we use @property  to access protected  caleed accesspost


zaib.username="sajid"
zaib.setpassword("sajid@123")
zaib.accesspost="zaib.png"
zaib.accesspost="dsa.png"


print(zaib.username)
print(zaib.getpassword())
print(zaib.accesspost)