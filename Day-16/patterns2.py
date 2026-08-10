"""n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()"""

"""
n=int(input())
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
 
    print()"""


""" 
output:
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
        """


"""

n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0  or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
    """
"""
* * * * * 
*       * 
*       * 
*       * 
* * * * * """

"""
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0  or i==n-1 or j==0 or j==n-1) or (i==n//2 or j==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() """
"""
* * * * * 
*   *   * 
* * * * * 
*   *   * 
* * * * *
"""
"""
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() """


#cccccccccccccccccchhhhhhhhhhhhhhhhheeeeeeeeeeeeeeeekkkkkkkkkkkkk aaaaaaaaabbbbbbbbbbbbooooooveeeeeeeeeee
#A
"""
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0  or i==n//2 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    """

#b
"""n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0  or i==n//2 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""


#C
"""
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0  or i==n-1 or j==0 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""


#D
"""n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0  or i==n-1 or j==0  or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""



#E

"""
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0  or i==n-1  or i==n//2 or j==0 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""


#F
"""n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0  or i==n//2 or j==0 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""


#G
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0  or j==0 or (i==n-1 and j<=m) or (j==m and i>=m) or(i==m and j>=m) or (j==n-1 and i>=m)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""
"""
* * * * * 
*         
*   * * * 
*   *   * 
* * *   *

"""

"""

n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0 or j==0) or (i==n-1 and j<=n//2) or (j==n//2 and i>=n//2) or (i==n//2 and j>=n//2) or (j==n-1 and i>=n//2 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""


#k gahr
"""
n=int(input())
for i in range(n):
    for j in range(n):
        if (j==0 or (i==n//2 and j<=n//2) or (i+j==n-1 and i<=n//2) or (i==j and i>=n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
"""
*       * 
*     *   
* * *     
*     *   
*       * 
"""



"""n=int(input()) 
for i in range(n):
    for j in range(n):

        if ((j==i) or (j==n-i-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()"""



"""
*       * 
  *   *   
    *     
  *   *   
*       * 

 """


#M
"""n=int(input())
for i in range(n):
    for j in range(n):
        if (j==0 or j == n-1 or (i==j and j<=n//2)  or (j==n-i-1 and i<=n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""


"""
*       * 
* *   * * 
*   *   * 
*       * 
*       *   
"""



"""
#K KKKKKKKKKKKKKKKKKKKKKKKKKKKK
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0  or (j==n-i-1 and i<=n//2) or (i==n//2 and j<=n//2) or (i>=n//2 and j==i):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()
"""
"""
n=int(input())
for i in range(n):
    for j in range(n):
        if (j==0 or (i==n//2 and j<=n//2) or (i+j==n-1 and i<=n//2) or (i==j and i>=n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

                                                                    """




#y
"""n=int(input())
for i in range(n):
    for j in range(n):
        if (j==i and i<=n//2 ) or (j==n-i-1 and  i <=n//2 ) or (j==n//2 and i>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""


"""
*       * 
  *   *   
    *     
    *     
    *   """

#vvvv

"""
n=int(input())
for i in range(n):
    for j in range(n):
        if (j==0 and i<=n//2) or (j==n-1 and i<=n//2) or (i-j==n//2 and i>=n//2) or (i+j==n//2+n-1 and i>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""



"""n=int(input())
for i in range(n):
    for j in range(n):
        if (j==0 and i<=n//2) or (j==n-1 and i<=n//2) or (i)
        
        """