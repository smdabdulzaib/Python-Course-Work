
##############Recursion#####################


"""
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)

display(1)
"""
"""
#output 
1
2
3
4
5
6
7
8
9
10
"""

"""
def display(n):
    if n>120:
        return
    print(n)
    display(n+1)

display(10) 
"""


#sum of numbers using recursion
"""
def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)

print(displaysum(8))
"""
#output 36

#product
"""
def displayproduct(n):
    if n==1:
        return 1
    return n*displayproduct(n-1)

print(displayproduct(4))
"""
#output: 24


#reverse a string:
"""

def display(ind):
    if ind==len(s):
        return
    print(s[ind])
    display(ind+1)
    

s="pyton"
display(0)"""


#0utput
"""
p
y
t
o
n"""



"""

def display(ind):
    if ind==len(s):
        return l
    l=l+s[i]
    print(l)
    retun display(ind+1,l)
    

s="pyton"
display(0)"""





"""
def display(n):
    if n>len(s):
        return
    print(s[:n])
    display(n+1)

s="python"
display(1)"""


"""def display(ind,w):
    if ind >len(s)-w:
        return
    print(s[ind:ind+w])
    display(ind+1,w)

s="python programming"
display(0,10)"""


"""
def display(n):
    if n==0:
        return
    display(n//10)
    print(n%10)
n=343134
display(n) 
"""


"""
def display(n):
    if n==0:
        return
    display(n//10)
    print(n%10)
n=343134
display(n) 

"""