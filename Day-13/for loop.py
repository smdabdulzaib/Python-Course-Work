"""s="python proramming"
for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        print(i,s[i])

"""






#sum of indexes of even numbers in a list
"""
l=[23,45,12,34,50,24,32,54,63,45,52]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+l[i]
        print(i,l[i])
print(sum)"""


#factorial of a number
"""
n=int(input("enter the number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(f"Factorialof {n} is {fact}")"""





#create a dictionary asking how many inputs and give max marks who scored
"""
data={}
n=int(input("Enter no of students: "))
max_marks=0
for i in range(n):
    name=input("enter name: ")
    marks=int(input("enter marks: "))
    if marks>max_marks:
        max_marks=marks
    data[name]=marks
print(data)
print(max_marks)
    """



#create aproduct name price and quantity and print final result of that with items if 2 laptops of price 40 result=40*2=80
"""
data={}
n=int(input("Enter how many products: "))

for i in range(n):
    product=input("Enter product name: ")
    price=int(input("Enter product price: "))
    quantity=int(input("Enter product quantity: "))
    data[product]=price*quantity

print(data)
"""


#billing statement 

"""
n=int(input("enter the no of products: "))
total=0
products={}
for i in range(n):
    product=input("product:")
    price=int(input("price:"))
    quantity=int(input("quantity:"))
    final_price=price*quantity
    total+=final_price
    products[product]=f"{price}*{quantity}={final_price}"
print(products)
print("Total Bill:",total)
"""




