"""import re
fullname=input("Enter the  full name:")
pattern=r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'

res=re.fullmatch(pattern,fullname)
print("valid full name"if res else "Invalid full name ")
"""


"""
import re
email=input("Enter the email: ")
pattern=r'^[a-zA-z0-9._]+@[a-zA-z0-9]+\.[a-zA-Z]{2,}$'
res=re.fullmatch(pattern,email)
print("Valid Email" if res else "Invalid Email")"""







"""
import re
phonenumber=input("Enter the phone Number:")
pattern=r'^(?:\+91|0)?[6-9]\d{9}$'

res=re.fullmatch(pattern,phonenumber)

print("valid number " if res else "invalid number")

"""







"""
import re 
password=input("Enter the password:")
pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\d)(?=.*[@%$!?&])[A-Za-z\d@$!%*?&]{8,}$' 
res=re.fullmatch(pattern,password)
print("Valid password" if res else "invalid Password")

"""


import re 
user_name=input("Enter the name:")
patterns=r'^[A-Z][a-z]{1,24}( [A-Z][a-z]{1,24})+$'
res=re.fullmatch(patterns,user_name)
print("valid user name " if res else "Invalid User Name")