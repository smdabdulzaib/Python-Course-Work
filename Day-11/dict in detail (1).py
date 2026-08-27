Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = {"name" :"sajid" , "batch" : 63, "course" : "pfs"}
>>> data["name"]
'sajid'
>>> data["batch"]
63
>>> data["course"]
'pfs'
>>> 63 in data
False
>>> #BECAUSE IT ONLY TAKES KEYS NOT VALUES :
>>> 
>>> data.get("age","key is not present")
'key is not present'
>>> data.get("course,"key is not present")
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> data["batch"] = 64
...          
>>> data
...          
{'name': 'sajid', 'batch': 64, 'course': 'pfs'}
>>> 
>>> data["skills"] = ["python","mysql","flask"]
...          
>>> data
...          
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask']}
>>> data["age"] = 21
...          
>>> data
...          
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
>>> #IF WE WANT TO UPDATE A LARGE AMOUNT OF DATA WE NEED TO USE .UPDATE()
...          
>>> data.update({"phno" : 8074630227 , "gmail" : "shaiksajid@gmail.com"})
...          
>>> data
...          
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8074630227, 'gmail': 'shaiksajid@gmail.com'}
>>> 
>>> 
>>> data.pop("age")
         
21
data
         
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'phno': 8074630227, 'gmail': 'shaiksajid@gmail.com'}
data.pop("phno")
         
8074630227
data
         
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'gmail': 'shaiksajid@gmail.com'}
data.popitem()
         
('gmail', 'shaiksajid@gmail.com')
data
         
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask']}
data.popitem()#IT IS USED TO REMOVE LAST KEY VALUE:
         
('skills', ['python', 'mysql', 'flask'])
data
         
{'name': 'sajid', 'batch': 64, 'course': 'pfs'}
data.clear()#IT WILL CLEAR ALL THE DATA
         
data
         
{}
data = {'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8074630227, 'gmail': 'shaiksajid@gmail.com'}
         
data.keys()
         
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phno', 'gmail'])
#.KEY () GIVES ONLY KEYS
         
data.values()
         
dict_values(['sajid', 64, 'pfs', ['python', 'mysql', 'flask'], 21, 8074630227, 'shaiksajid@gmail.com'])
#VALUES() GIVES ONLY VALUES
         
max(data)
         
'skills'
min(data)
         
'age'
sorted(data)
         
['age', 'batch', 'course', 'gmail', 'name', 'phno', 'skills']
sorted(data,reverse = True)
         
['skills', 'phno', 'name', 'gmail', 'course', 'batch', 'age']
data["age"]
         
21
data
         
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8074630227, 'gmail': 'shaiksajid@gmail.com'}
data.get("age")
         
21
data.setdefault("age",0)
         
21
data
         
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8074630227, 'gmail': 'shaiksajid@gmail.com'}
data.setdefault("name , "")
                
SyntaxError: incomplete input
data.setdefault("name" , " ")
                
'sajid'
data
                
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8074630227, 'gmail': 'shaiksajid@gmail.com'}
len
                
<built-in function len>
data
                
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8074630227, 'gmail': 'shaiksajid@gmail.com'}
data["gender"] = "male"
                
data
                
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8074630227, 'gmail': 'shaiksajid@gmail.com', 'gender': 'male'}
data.popitem()
                
('gender', 'male')
data
                
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8074630227, 'gmail': 'shaiksajid@gmail.com'}
data.setdefault("gender"," ")
                
' '
data
                
{'name': 'sajid', 'batch': 64, 'course': 'pfs', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8074630227, 'gmail': 'shaiksajid@gmail.com', 'gender': ' '}
