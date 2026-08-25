"""
fa = eval(input("follows account: "))
ca = eval(input("close friends : "))
if fa:
    if ca:
        print("story visible")
    else:
        print("you are not in close friend list")
else:
    print("follow account first") 
    """   
"""
reg = eval(input("registered :"))

if reg:
    fee = eval(input("fee :"))
    if fee:
        print(" entry confirmed")
    else:
        print("entry fee pending ")
else:
    print("Regestration Required ")                      

    """

lin = eval(input("file Liknked :"))

if len:
    dis = eval(input("Permission : "))
    if dis:
        print("File opened succesfully")
    else:
        print("acces dinied")
else:
    print("invalid file Link")            
