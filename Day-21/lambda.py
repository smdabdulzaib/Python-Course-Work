########Lambda functions


#greatest number
greater=lambda a,b: a if a>b else b
print(greater(12,14))
print(greater(44,11))
print(greater(232,5323))

#output
"""
4
44
5323"""




wish=lambda name:f'Welcome to the course  {name}'
print(wish("Sajid"))
print(wish("zaib"))
print(wish("abdul"))

#Welcome to the course  Sajid
#Welcome to the course  zaib
#Welcome to the course  abdul



iseven=lambda n:"Even" if n%2==0 else "odd"
print(iseven(2))
print(iseven(34))
print(iseven(32123))
print(iseven(1))

#Even
#Even
#odd
#odd




avg=lambda a,b,c:(a+b+c)/3
print(avg(2,4,3))
print(avg(2,3,9))
print(avg(2,2,2))

#3.0
#4.666666666666667
#2.0




domain=lambda mail: (mail.split('@')[-1]).split(".")[0]


print((domain("sowmya@codegnan.com")))
print((domain("sowmya@gmail.com")))
print((domain("sowmya@outlook.com")))
print((domain("sowmya@yahoo.com")))

#output
#codegnan
#gmail
#outlook
#yahoo




gst=lambda price : price+price*0.18

print(gst(1000))
print(gst(5000))
print(gst(8000))

"""
1180.0
5900.0
9440.0"""

#list using lambda
prices=[3432,4342,2134,8754,3456,7654]
res=list(map(lambda price: price+price*0.18,prices))
print(res)


#[4049.76, 5123.5599999999995, 2518.12, 10329.72, 4078.08, 9031.72]




#can be ste ,tuple,list 
names=["zaib","sajid","dee","saa"]

res=list(map(lambda name:name.title(),names))

print(res)

#outppt
#['Zaib', 'Sajid', 'Dee', 'Saa']


prices=[3432,4342,2134,8754,3456,7654]
res=list(map(lambda price: price-price*0.3,prices))
print(res)

#[2402.4, 3039.4, 1493.8000000000002, 6127.8, 2419.2, 5357.8]




#filter
#greater than 5000
prices=[3432,4342,2134,8754,3456,7654]
res=list(filter(lambda price:price>5000,prices))
print(res)

#[8754, 7654]


#odd
prices=[3432,4342,2133,8753,3456,7654]
res=list(filter(lambda price:price%2!=0,prices))
print(res)


#[2133, 8753]



names=["abdsdul","sajid","dee","saa"]

res=list(filter(lambda name:len(name)>5,names))

print(res)
#['abdsdul']







#reduce used to combine all input values present

from functools import reduce
l=[3,567,32,435,435,462]
res=reduce(lambda sum,i:sum+i,l)
print(res)


names=["zaib","sajid","dee","saa"]
res=reduce(lambda res,i: res+""+i,names)
print(res)

#1934
#zaibsajiddeesaa 


products={'sugar':60,
          'salt':50,
          'egg':90,
          'cooking oil':120,
          'bread':45
          }




print(dict(sorted(products.items())))

print(dict(sorted(products.items(),reverse=True)))

print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))




