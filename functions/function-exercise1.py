# to print table in reverse order

def table(n):
    i=10
    while(i>=1):
        t=n*i
        print(n,'*',i,'=',t)
        i=i-1

x=int(input('enter the number for table:'))
table(x)
