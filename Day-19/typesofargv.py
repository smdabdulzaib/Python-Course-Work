
#Arguments

#positional Arguments
#keyword arguments
#Default Arguments
#Variable length postional Argument  *,**   *args,**kwargs






#positional Arguments

"""
def display(name,email,password):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')

display("xyz",'xyz@gmail.com','xyz@123')
display("kis","asfae@gmail.com","asde@ma")
display("deef","adef@gmail.com","fdaf@mma")
"""



#keyword arguments
#based on keys it maps 

"""
def display(name,email,password):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')

display(name="xyz",email='xyz@gmail.com',password='xyz@123')
display(email="kis",password="asfae@gmail.com",name="asd")
display(password="deef",name="adef@gmail.com",email="fdaf@mma")


"""




#Default Arguments
#FIRST IT CHECK IVEN AVALUS AFTER THATT IF NOT FOUND IT GOES TO arguments
"""
def display(name,email="GMAIOL.COM",password=""):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')


display("xyz",'xyz@gmail.com','xyz@123')
display("kis","asfae@gmail.com")
display("deef")"""




#output:

'''
output:name:xyz
email:xyz@gmail.com
password:xyz@123
name:kis
email:asfae@gmail.com
password:
name:deef
email:GMAIOL.COM
password:
'''





#Variable length postional Argument
#tuple format its getting

"""def display(*names):
    print(names)


display("zaib")
display("zaib","sajid")
display("lijs","ijijd","kujsd","nsd")"""


#output:
'''
('zaib',)
('zaib', 'sajid')
('lijs', 'ijijd', 'kujsd', 'nsd') 

'''


#key value
"""
def display(**products):
    print(products)

display(bag=500)
display(bag=5000,book=30)
display(bag=9923,book=93487,bottle=2394)"""


#output 
"""
{'bag': 500}
{'bag': 5000, 'book': 30}
{'bag': 9923, 'book': 93487, 'bottle': 2394} 
"""