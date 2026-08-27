"""
f = open("myfiles.txt","r")
print(f.read())
f.seek(0)
print(f.readline())
f.seek()
print(file.readlines())
f.close()

with open("myfiles.txt","r")as f: 
 print(f.read(0))
 f.seek()
 print(f.readline())
 f.seek()
 print(f.readlines())
 f.close()  

with open ("myfiles.txt","w") as file:
    file.write("sajid is cool")

with open("myfiles.txt","a")as file:
    file.write("sajid is also better")  
    """
with open("myfiles.txt","a+") as file:
    file.write("tomorrow to same branch 5")
    file.seek(0)
    print(file.read())

