
import sys 
"""
print(sys.path) # ALL THEDATA THAT THE FILE CONTAION IN ANOTHER FORMAT AS OUT PUT
print(sys.version) #SHOEWS WHICH VERSION IS YOUR PYTHON
print("start")
sys.exit()
print("end")

import platform 
print(platform.system())
print(platform.release())
print(platform.processor())

import math
print(math.pi)
print(math.e)

print(math.sqrt(36))
print(math.pow(2,3))

print(math.ceil(12.0001))#CEIL() GIVE U THE UPPER VALUE JUST REMEBER CEIL ME UPPER SO IT GIVES PEER VALUE
print(math.ceil(12.6))
print(math.ceil(12.3))
print(math.ceil(12.9999))

print(math.floor(12.001)) #FLOOR () GIVES LOWER VALUE JUST REMEBER FLOOR MEANS GROUND SO IT GIVES LOWER VALUE
print(math.floor(12.3))
print(math.floor(12.4))
print(math.floor(12.1000))

print(math.fabs(-10))# FAB () DOES NOT GIVE NEGETIVE VALUES
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
"""

"""
import random
#random.seed(10) ITS IS USED WHEN WE WANT TO STICK TO THE SAME NUMBER WE GIVE LIKE "SEED(10)"
print(random.randint(1,10))
print(random.randint(100000,999999))
print(random.random()) #IT GIVES US FLOATING POINT NUMBER RANDOM.RANDOM()
print(random.uniform(1,6))

l = ["R","P","S"]
print(random.choice(l))
print(random.choices(l,k=2))#IF WE MANY CHOICES WE CHIICE'S() AND K =2 SO WE GET TWO OUT PUT

random.shuffle(l)
print(l)

"""
from collections import Counter,defaultdict,deque

s = " python programing"
m = "this is that that is this is".split()
l = [1,21,1,1,1,2,3,4,44,4,4,4,4,32,22,21,21,21,21,21,32,32,32,32,32]
"""
print(counter(s))
print(counter(m))
print(counter(l))

d = defaultdict(int)
for i in s:
    d[i]+=1
print(d)

d = defaultdict(str)
for i in s:
    d[i]+="1"
print(d)
"""
"""
l = deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(50)
l.append(70)
l.popleft()
print(l)

l = deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.popleft()
l.popleft()
l.appendleft(50)
l.appendleft(70)
l.popleft()
print(l)
"""

from itertools import combinations,permutations
res1 = list(combinations("ABC",2)) 
res2 = list(permutations("ABC",2))
print(["".join(i) for i in res1])
print(["".join(i) for i in res2])









