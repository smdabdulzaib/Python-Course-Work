"Process where child class acquires properties and methods of parent call "
"for code reusibility and avoid rewriting  same code"
#single level inheritence(1parent ,1child)

#multi level inheritence(grand,parent,child)

#multiple inheritence(1 child ,many parents)

#hierarchical inheritence(1parent,many childs)

#Hybrid inheritence -mix of  all



#____________________________________________single level inheritence(1parent ,1child)

class whatsappv1:
    def messaging(self):
        print("you can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can aaudio and video calls")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()




# ______________________________________multi level inheritence((grand,parent,child))
class whatsappv1:
    def messaging(self):
        print("you can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can aaudio and video calls")
class whatsappv3(whatsappv2):
    def status(self):
        print("You can add staus now")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()



c=whatsappv3()
c.messaging()
c.calls()

c.status()




#
class whatsappv1:
    def messaging(self):
        print("you can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can aaudio and video calls")
class whatsappv3(whatsappv2):
    def status(self):
        print("You can add staus now")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()



c=whatsappv3()
c.messaging()
c.calls()

c.status()


#_________________________________________multiple inheritence(1 child ,many parents)

class whatsappv1:
    def messaging(self):
        print("you can message")
class whatsappv2:
    def calls(self):
        print("you can aaudio and video calls")
class whatsappv3(whatsappv1,whatsappv2):####
    def status(self):
        print("You can add staus now")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.calls()



c=whatsappv3()
c.messaging()
c.calls()
c.status()










#______________________________________hierarchical inheritence(1parent,many childs)  ______________hierarchical hierarchical

class whatsappv1:
    def messaging(self):
        print("you can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can aaudio and video calls")
class whatsappv3(whatsappv1):####
    def status(self):
        print("You can add staus now")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.calls()



c=whatsappv3()
c.messaging()
#c.calls()
c.status()





#________________________#Hybrid inheritence -mix of all

class whatsappv1:
    def messaging(self):
        print("you can message")

class whatsappv2:
    def extra_messagings(self):
        print("you can message emojis , strickers also")

class whatsappv3(whatsappv1,whatsappv2):    #multiple inheritence
    def calls(self):
        print("you can aaudio and video calls")

class whatsappv4(whatsappv3):#### multi level inheritence 
    def status(self):
        print("You can add staus now")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.extra_messagings()



c=whatsappv3()
c.messaging()
c.extra_messagings()
c.calls()



d=whatsappv4()
d.messaging()
d.extra_messagings()
d.calls()
d.status()




#when we have same method name we use ""super().method name()""
#should be same method we use super().methodname()


class whatsappv1:
    def statuss(self):
        print("you can  add images and videos")

class whatsappv2(whatsappv1):
    def statuss(self):
        print("you can  add music and stickers")
class whatsappv3(whatsappv2):
    def statuss(self):
        print("you can like and react also ")


#if u print only like 
k=whatsappv2()
k.statuss()  #u only get you can  add music and stickers but not get immages and videros so we use super  now 




class whatsappv1:
    def statuss(self):
        print("you can  add images and videos")

class whatsappv2(whatsappv1):
    def statuss(self):
        super().statuss()
        print("you can  add music and stickers")
class whatsappv3(whatsappv2):
    def statuss(self):
        super().statuss()
        print("you can like and react also ")

k=whatsappv2()
k.statuss() #you get both music stickers imaes and videos

z=whatsappv3() #u get all as we use super()..
z.statuss()





#class inheritencee,, use always ""class name. method name (self)""  

class whatsappv1:
    def statuss(self):
        print("you can  add images and videos")

class whatsappv2:
    def statuss(self):
        print("you can  add music and stickers")
class whatsappv3(whatsappv1,whatsappv2):
    def statuss(self):
        whatsappv1.statuss(self)   #use class name .method name (self)
        whatsappv2.statuss(self)
        print("you can like and react also ")

a=whatsappv3()
a.statuss()