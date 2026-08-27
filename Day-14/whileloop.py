"""i=1
while i<=10:
    print(i)
    i+=1


i=10
while i>10:
    print(i)
    i-=1"""



"""
i=2
while i<=100:
    print(i) #with want output sideby side we use print(i,end=" "),ifneed bu couma then end=","
    i+=2
    """

"""
#reverse a string using while loop
s="python programming"

i=len(s)-1
while i>=0:
    print(s[i],end="")
    i-=1

    """



#remove 0 from list of numbers
"""l=[1,0,0,0,0,2,5,3,2,5,6,7,7,0,0,0,4,8,0,9]
while 0 in l:
    l.remove(0)
print(i)  """





#billinng
"""data={}

while True:
    product=input("enter product:")
    if product =="exit":
        break

    price=int(input("enter price:"))
    data[product]=price

print(data)"""  #when exit click it stops the {'apple': 22, 'u ': 23, 'ub': 53

"""
data={}

total_bill=0
while True:
    product=input("enter product:")
    if product =="exit":
        break

    price=int(input("enter price:"))
    total_bill+=price
    data[product]=price

print(data)
print("total_bill is:",total_bill)"""


"""
#Else with while 
i=0
while i<=10:
    i+=1
    if i ==5:
        break
    print(i)
else:
    print("end of loop")  #oupt:1 2 3 4


i=0
while i<=10:
    i+=1
    if i ==15:
        break
    print(i)
else:
    print("end of loop")   #ouptput 1 2 3 4 5 6 7 788 9 10 end of loop"""
