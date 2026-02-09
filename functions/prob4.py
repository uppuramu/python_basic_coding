# get avarage of n values

def avg(n):
    sum=0
    for i in range(0,n):
        num=int(input('enter number:'))
        sum=sum+num
    a=sum/n
    print('avarage of',n,'numbers is:',a)

x=int(input('enter total number of values:'))
avg(x)
