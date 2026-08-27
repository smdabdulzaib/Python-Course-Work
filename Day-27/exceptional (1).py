"""
try :
    a = int(input())
except ValueError:
    print("enter correct data type")
else:
    print("a=",a)
finally:
    print("end of the program")  
    
try :
    # a = int(input())
     k = {1:12,2:44}
     print(k[14])
     l = [407,4730]
     print(l[410])
     print(10/0)
     print("1"+1)
except ValueError:
    print("enter correct dat type")
except KeyError:
    print("key is not there")
except IndexError:
    print("index is out of range")
except ZeroDivisionError:
    print("cant divide with zero")
except NameError:
    print("define the varrialbel")
else:
    print("error free programing")
finally:
    print("end of program")  

try :
    # a = int(input())
     k = {1:12,2:44}
     print(k[14])
     l = [407,4730]
     print(l[410])
     print(10/0)
     print("1"+1)

except(ValueError,KeyError,IndexError,ZeroDivisionError,TypeError,NameError ) as e:
    print("error occured:",e) # INSTEAD OF DOING LIKE ABOVE BIG WE CAN GIVE ALL THE ALL ERROR IN ONE FRAME:
else:
    print("error free program")
finally:
    print("end o the program")    
   

try :
    # a = int(input())
     k = {1:12,2:44}
     print(k[14])
     l = [407,4730]
     print(l[410])
     print(10/0)
     print("1"+1)
except Exception as e: # EXCEPT EXCEPTION AS E IS USED FOR ERROR NOT VISIBEL:
    print("Error Occured :",e)
else:
    print("Error Free Code")
finally:
    print("End of Program")   
    """
try :
    amount = int(input("enter your amount :"))
    balance = 500
    if amount < 0:
        raise Exception ("amount must be in postive")
except Exception as e:
    print("error occured")
else:
    print("erroer free program")
finally:
    print("end of the program")                

         
    



