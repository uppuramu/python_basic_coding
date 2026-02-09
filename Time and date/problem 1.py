# get two dates from user find their diffrence in days

from datetime import *
d1=int(input('day:'))
d2=int(input('day:'))

m1=int(input('month:'))
m2=int(input('month:'))

y1=int(input('year:'))
y2=int(input('year:'))

d1=date(y1,m1,d1)
d2=date(y2,m2,d2)
day=d2-d1
print(day.days)