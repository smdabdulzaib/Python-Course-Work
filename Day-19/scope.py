"""
def display(n):
    n=n+10
    print('Inside:',n)


n=10
display(n)
print('outside:',n)
"""

#output
#Inside: 20
#outside: 10


"""def display():
    print('Inside:',n)


n=10
display()
print('outside:',n)"""

#output
#Inside: 10
#outside: 10





"""
def display():
    n=10
    print("inside:",n)

display()
print("outside:",n)
"""
#output 
#inside: 10
#ouside :NameError: name 'n' is not defined as no global varible assigned


##############GLOBAL 
#access global if changes made in inner shpould effect global then we take ""glabl n ""
#also effect both inner and global
"""
def display():
    global n
    n=n+10
    print("inside:",n)

n=10
display()
print("outside:",n)"""

#output
#inside: 20
#outside: 20

###############Global


"""
def display():
    global n
    n="PFS"
    print("updated",n)
n="ZAZA"
display()
print("Final Course:",n)

"""
 

#output
#updated PFS
#Final Course: PFS











#############non local#####33
"""
def display():
    n="jfs"
    def update():
        n="zaza"
        print("updated:",n)
    update()
    print("final:",n)

display()
"""

#OUPTPUT:
# updated: zaza
#final: jfs

"""
def display():
    n="jfs"
    def update():
        nonlocal n
        n="zaza"
        print("updated:",n)
    update()
    print("final:",n)

display()


"""
#updated: zaza
#final: zaza