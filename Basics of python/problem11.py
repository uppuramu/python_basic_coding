# get a sequence of numbers between first and ending number taken by user as input
# must check starting number less than the ending number

m=int(input('enter starting number:'))
n=int(input('enter ending number:'))
s=m
while(m<=n):
    print(m)
    m=m+1
if(s>n):
    print('given input in the wrong format')