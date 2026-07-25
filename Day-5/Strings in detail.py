Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#slicing
s="codegnan"+"hyd"
s
'codegnanhyd'


s="zaib"*10
s
'zaibzaibzaibzaibzaibzaibzaibzaibzaibzaib'

s="zaib sajid are here"
s[1]
'a'
s[3]
'b'
s[0:4]
'zaib'
s[-1]
'e'
s[::-1]
'ereh era dijas biaz'
s
'zaib sajid are here'
>>> s[1::]
'aib sajid are here'
>>> s[::}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s[::]
'zaib sajid are here'
>>> #here
>>> s=[-1:-5:-1]
SyntaxError: invalid syntax
>>> s=[-1:-5]
SyntaxError: invalid syntax
>>> s[::2]
'zi ai r ee'
>>> s[-1:-2]
''
>>> 
>>> s[-1:-4]
''
>>> s[::-1]
'ereh era dijas biaz'
>>> s[-1:-5:-1]
'ereh'
>>> s[-1:-5]
''
>>> s[::-1]
'ereh era dijas biaz'
>>> 
>>> ''sajid'' in s:
...     
SyntaxError: invalid syntax
>>> "zaib" in s
True
>>> "sajid" in s
True
>>> "kin" not in s
True
>>> "i" in s:
...     
SyntaxError: invalid syntax
>>> "i" in s
True
>>> "o" in s
False
