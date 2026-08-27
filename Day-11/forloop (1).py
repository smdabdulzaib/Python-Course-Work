""" for var in seq:
        print(var)
        """
"""
s = " codegnan"
for ch in s:
    if ch in "aeiou":
        print("ch")
        """
"""
for i in range (1,11):
    print(i)
    """
"""
l =[10,23,4,5,14,33,52,22]
for i in l:
    if i%2==0 :
        print(i,"even")
    else:
        print(i,"odd") 
        """
"""
marks = (35,33,45,90,77,44)
for i in marks:
    if i >= 35: 
        print(i,"pass")
    else:
        print(i,"fail")                            

        """

"""
followers = {"Sajid","Faheem","Taha","Ruhan","Athif","Ashraf","Zaib"}
for i in followers:
    print(i)        

    """
"""
bus= {"s1":"booked","s1":"avilable","s1":"booked","s1":"avilable","s1":"booked"}
for i in bus:
    if bus.get(i)  == "avilable":
        print(i, bus.get(i))
        """

#RANGE (SRATR,END+1,STEP) ==> (0,NODEF,1)
"""
for i in range(1,11):
    print(i) """
"""
for i in range(2,51,2):
    print(i, end = " ")#IF WE WANT THE OUTPUT IN SAME LINE WE USE END =" "
"""
"""
for i in range(1,100,2):
    print(i,end = " ")   
    """
n = int(input("Enter Your Tabel :"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")       



        
    

