Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={}
type(s)
<class 'dict'>
s=set()
type(s)
<class 'set'>
s={1,2,3,4,12,234,213,536,5745,7865}
s
{1, 2, 3, 4, 234, 12, 5745, 213, 536, 7865}
s.add(1)
s.add(12.3)
s.add(2+4j)
a.add()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.add()

s
{1, 2, 3, 4, 234, 12, 12.3, (2+4j), 5745, 213, 536, 7865}
#ismutable only for only immutable data types
s={11,1,,1,1,1,1,11,1,1,1,}
SyntaxError: invalid syntax
s={1,1,2,,3,3,32,2,1,1,1,1,1,1}
SyntaxError: invalid syntax
s={1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2}
s
{1, 2}
l={10,20,30}
m={1,23,34}
#cant do indexing ,concattenating,reptin
a={1,23,4,52,32}
b={24,521,442,234,23,52}
a
{32, 1, 4, 52, 23}
b
{442, 52, 23, 24, 521, 234}
a|b
{32, 1, 4, 521, 234, 52, 23, 24, 442}
a|b#union its called mixing both without alllowing dupliacte common elemnts
{32, 1, 4, 521, 234, 52, 23, 24, 442}
a&b#intersextion only common would come
{52, 23}
a-b
{32, 1, 4}
{32, 1, 4}#onlyelemts in a will appear without any b elemts or coomin
{32, 1, 4}

a^b
{1, 4, 521, 24, 32, 234, 442}
#other can common all appear
{1} <=a
True
{1,23,4,52}<=a
True
a={1,2,3,4,5}
b={9,3,5,7}
a.isjoint
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.isjoint
AttributeError: 'set' object has no attribute 'isjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
a.isdisjoint({9,10})
True

#disjoint means not avilabel means true it et
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubbset(b)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.issubbset(b)
AttributeError: 'set' object has no attribute 'issubbset'. Did you mean: 'issubset'?
a.issubset(b)
False
a.issuperset(b)
False
a={1,2,4,6,7}
5 in a
False
#membership
6 in a
True
8 not in a
True
7 in a
True
0 in a
False
max(a)
7
min(a)
1
sum(a)
20
a={1,2,3,4,5}
b=a

b.add(12)

b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c=a.copy()
c.add(12)
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
#add multiple use update
a.update({16,17,18})
a
{1, 2, 3, 4, 5, 12, 16, 17, 18}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 12, 16, 17, 18}
#specific value if u need to delete then
a.remove(5)
a.remove(12)
#discard if alraedy deleted it handle error
a.dicard(5)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.dicard(5)
AttributeError: 'set' object has no attribute 'dicard'. Did you mean: 'discard'?
a.discard(5)
a.discard(12)
#for removve all set uses
a.clear()
a
set()
f
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    f
NameError: name 'f' is not defined
a.update({"str",1,,32,2,-12,323}]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
a.update({"str",1,,32,2,-12,323})
SyntaxError: invalid syntax
KeyboardInterrupt
KeyboardInterrupt
a.update({"str",1,42,32,2,-12,323})
a
{32, 1, 2, 323, -12, 'str', 42}
len(a)
7
all(a)
True
a=frozenset({1,2,3,4,2,202,2})
a.add(13425200)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.add(13425200)
AttributeError: 'frozenset' object has no attribute 'add'
AttributeError: 'frozenset' object has no attribute 'add'
SyntaxError: invalid syntax








d={}
d=dict()
type(d)
<class 'dict'>
d={'ki':'v1','k2':'v2','k3':'v3'}
d
{'ki': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
1628531497024
d['k4']='v4'
id(d)
1628531497024
d[12.3]='flt'
d
{'ki': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 12.3: 'flt'}
d[12+3j]="com'
SyntaxError: unterminated string literal (detected at line 1)
>>> d[12+3j]="com"
>>> d[(1,2,3,4,6,3)]='tuple'
>>> d
{'ki': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 12.3: 'flt', (12+3j): 'com', (1, 2, 3, 4, 6, 3): 'tuple'}
>>> 
>>> d={}
>>> d[1]=1
>>> d[2]=12.3
>>> d[3]=12+4j
>>> d[4]="str"
>>> d[5]=[12,3,4,5,2]
>>> d[6]=(1,3,4,5)
>>> d[6]={1,2,3}
>>> d[7]={1:1}
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [12, 3, 4, 5, 2], 6: {1, 2, 3}, 7: {1: 1}}
>>> {1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [12, 3, 4, 5, 2], 6: {1, 2, 3}, 7: {1: 1}}
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [12, 3, 4, 5, 2], 6: {1, 2, 3}, 7: {1: 1}}
>>> 
>>> 10 in d
False
>>> 4 ind
SyntaxError: invalid syntax
>>> 4in d
True
>>> d[5]
[12, 3, 4, 5, 2]
>>> d[8]
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    d[8]
KeyError: 8
>>> d[7]
{1: 1}
>>> d.get(7)
{1: 1}
>>> d.get(10,"key is not present")
'key is not present'
>>> d.get(6,"key is not present")
{1, 2, 3}
>>> d[6]=12
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [12, 3, 4, 5, 2], 6: 12, 7: {1: 1}}
