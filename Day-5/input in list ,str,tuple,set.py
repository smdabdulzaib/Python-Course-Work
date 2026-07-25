Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=input()
jsomsub
x
'jsomsub'
name=input()
zaib
name
'zaib'
age=input()
21
age
'21'
age=int(input())
21
ae
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ae
NameError: name 'ae' is not defined. Did you mean: 'age'?
age
21
age=int(input("enter age:"))
enter age:22
age
22
price=float(input())
2.034
price
2.034




names=input("enter names")
enter nameszaib sajid
names
'zaib sajid'
#so we use split to seperate names into differnt words
names=input("enter :").split()
enter :zaib sajid
names
['zaib', 'sajid']
#we need list of numbers then we use
numbers=input("enter:").split()
enter:22 3  34 4
numbers
['22', '3', '34', '4']
#they are in strings so we use map()
numbers=int(input("enter:").split())
enter:22 3 3 12 13 33
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    numbers=int(input("enter:").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
SyntaxError: invalid syntax





numbers=int(input("enter:"))
enter:22 34 231 12 3
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    numbers=int(input("enter:"))
ValueError: invalid literal for int() with base 10: '22 34 231 12 3'
ValueError: invalid literal for int() with base 10: '22 34 231 12 3'
SyntaxError: invalid syntax
num=int(input())
22 3 34 21 1
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    num=int(input())
ValueError: invalid literal for int() with base 10: '22 3 34 21 1'
num
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    num
NameError: name 'num' is not defined. Did you mean: 'sum'?
l=int(input())
3 23 23 23 12 15
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    l=int(input())
ValueError: invalid literal for int() with base 10: '3 23 23 23 12 15'
ValueError: invalid literal for int() with base 10: '3 23 23 23 12 15'
SyntaxError: invalid syntax
l=int(input())
2
l
2

#map
#but formultipple numbers in list we use
#but formultipple numbers in list we use
numbers=map(input("enter:").split())
enter:22 3 21 123 
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    numbers=map(input("enter:").split())
TypeError: map() must have at least two arguments.

numbers=map(int,input("enter:").split())
enter:2 232 1434 
numbers
<map object at 0x0000017B2346C460>
<map object at 0x0000017B2346C460>
SyntaxError: invalid syntax
numbers=map(int,input("enter:").split())
enter:2 232 2 12
numbers
<map object at 0x0000017B2346C040>
numbers=(int,input("enter:").split())
enter:2 232 2 12
numbers
(<class 'int'>, ['2', '232', '2', '12'])
(<class 'int'>, ['2', '232', '2', '12'])'
SyntaxError: unterminated string literal (detected at line 1)
numbers=list(map(int,input("enter:").split()))
enter:2 232 4 12
numbers
[2, 232, 4, 12]
[2, 232, 4, 12]
[2, 232, 4, 12]



#tuple
names=tuple(input().split())
zaib
names
('zaib',)
('zaib',)
('zaib',)


numbers=tuple(map(int,input("enter:").split()))
enter:1 223  43
numbers
(1, 223, 43)



#set
names=set(input().split())
hi jid d d
names
{'d', 'hi', 'jid'}
k=tuple(map(int,input("enter:").split()))
enter:2 34 5 3
k
(2, 34, 5, 3)


#dic


# multipkle inputs


a,b=[1,2]
#map to update each one we use map
a
1
b
2
a,b,c=int(input().split())
1
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a,b,c=int(input().split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
a,b,c=list(map(int,input().split()))
1 2 3 
a
1
b
2
c
3


names,loc=input().split()
nnqa jhij
names
'nnqa'
location
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    location
NameError: name 'location' is not defined
loc
'jhij'

 

names,age=input().split()
zaib 2 
names
'zaib'
ae
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    ae
NameError: name 'ae' is not defined. Did you mean: 'age'?
age
'2'
int(age)
2
age
'2'
>>> int(age)
2
>>> #all the obove is multiple inputs not dic
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #eval
>>> e=eval(input())
1
>>> e
1
>>> e=eval(input())

Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    e=eval(input())
  File "<string>", line 0
    
SyntaxError: invalid syntax
>>> 1234.13
1234.13
>>> 
>>> e
1
>>> es=eval(input())
1234.14
>>> es
1234.14
>>> e=eval(input())
"zaib"
>>> e
'zaib'
>>> m=eval(input())
2+2*4+6*6+3
>>> m
49
