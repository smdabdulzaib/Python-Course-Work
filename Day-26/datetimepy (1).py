from datetime import date,time,datetime,timedelta
"""
today = date.today()

print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

t = time(23,50,44)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

n = datetime.now()
print(n)
print(n.strftime("%d-%m-%y"))
print(n.strftime("%d-%m-%Y %H:%M:%S"))
print(n.strftime("%d %m %Y %H:%M:%S %p"))
print(n.strftime("%d %b %m %y %H:%M:%S:%P"))
print(n.strftime("%d %B %m %y %H:%M:%S:%P"))
print(n.strftime("%A, %d %B %m %y %H:%M:%S:%P"))
"""
t = date.today()
n = datetime.now()
t7 = t + timedelta(days=7)
t5 = t - timedelta(days=7)
n15 = n + timedelta(minutes=15)
print(t,t7,t5)
print(n,n15)
