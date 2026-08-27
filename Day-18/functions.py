#functions
"""
def display(name,email,password):
    print(f"hello {name}")
    print(f"Your email:{email}")
    print(f"your password{password}")

display("zaib","shaikzaib18@gmail.com","p@ssrddd")
display("sajid","sajidshaik@gmail","shaiksajid")
        """

"""
def isleapyear(year):
    if year%4==0 or (year%4==0 and year%100!=0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


for year in range(2001,2027):
    isleapyear(year)"""




"""
def sumofdigits(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10 
    return sum
n=int(input("enter the number: "))
print(f"sum of {n}digits is {sumofdigits(n)}")"""



#productofdigits
"""
def productofdigits(n):
    pro=1
    while n>0:
        pro*=n%10
        n=n//10 
    return pro
n=int(input("enter the number: "))
print(f"sum of {n}digits is {productofdigits(n)}")


"""




#password checker tht itsvalid strong password ornot 
"""

def checkpassword(password):
    if len(password)>8:

        check=set()
        for i in password:
           
           if i.isupper():
               check.add("u")
           elif i.islower():
               check.add("l")
           elif i.isdigit():
               check.add("d")
           else:
               check.add("s")
        if len(check)==4:
            return"strong password"
    return"week password "


password=input()
print(checkpassword(password))

"""


#tables



#########table'

"""
def table(n):
    print (f'___________________________Table- {n}_____________________')
    for i in range(1,11):
        print(f'{n}  *  {i}={n*i}')

for i in range(1,21):
    table(i)
   
    
     
       """