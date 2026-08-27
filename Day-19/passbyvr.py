#int,float,str,list,tuple,set,dict,bool


#int,float,str,tuple,bool-pass by value 
#list,set,dict-pass by object references

#int
"""
def display(n):
    n=4
    print("Inside:",n)

n=8
display(n)
print("outside:",n)

"""
#Inside: 4
#outside: 8



#float
"""
def display(n):
    n=4.5
    print("Inside:",n)

n=8.5
display(n)
print("outside:",n)

"""
#Inside: 4.5
#outside: 8.5



#str
"""
def display(n):
    n+="py"
    print("Inside:",n)

n="thon"
display(n)
print("outside:",n)"""

#Inside: thonpy
#outside: thon



#tuple
"""def display(n):
    n+=(3,4)
    print("Inside:",n)

n=(1,2,3,4,5)
display(n)
print("outside:",n)

"""

#Inside: (1, 2, 3, 4, 5, 3, 4)
#outside: (1, 2, 3, 4, 5)




#list


"""
def display(n):
    n+=[1,4]
    print("Inside:",n)

n=[1,2,3,4,5]
display(n)
print("outside:",n)
"""


#same

#Inside: [1, 2, 3, 4, 5, 1, 4]
#outside: [1, 2, 3, 4, 5, 1, 4]



"""#set
def display(n):
    n{1,4}
    print("Inside:",n)

n={1,2,3,4,5}
display(n)
print("outside:",n)"""