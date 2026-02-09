# find square root of a number and find square root of result
# add both results
from cmath import sqrt
import math
num=int(input('enter a number:'))
r1=math.sqrt(num)
r2=math.sqrt(r1)
sum=r1+r2
print(sum)
