"""for i in range(1,11):
    if i==5:
        break
    print(i)
else:
    print("END OF LOOP ")"""
        #output: 1 2 3 4




"""
for i in range(1,11):
    if i==15:
        break
    print(i)
else:
    print("END OF LOOP ")"""
    #output: 1 2 3 4 5 6 7 8 9 10 END OF LOOP

#if break is not executed then else will be executed otherwise not otherwise if break is executed then else will not be executed

"""
pin=5555
for i in range(5):
    epin=int(input("enter pin: "))
    if epin==pin:
        print("correct pin")
        break
    else:
        print("incorrect pin")
else:
    print("Try after 30 seconds")   """
#output: enter pin: 1234
#incorrect pin  


"""
#factors of numbers
n=int(input("enter the number: "))
print("Factors:",end=" ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")

"""



#prime number

"""n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1

if c==2:
    print("prime number")
else:
    print("NOT a prime number")



n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        c+=1

if c==0:
    print("prime number")
else:
    print("NOT a prime number")


n=int(input())
for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime ")"""

"""

#factorail
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)
"""
"""
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("not prime")    """
"""
n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        c+=1
if c==0:
    print("prime")
else:
    print("not prime")"""

"""
n=int(input())
for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime")
"""