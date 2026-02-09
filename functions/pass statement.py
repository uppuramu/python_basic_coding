# pass-  used for to pass a statement in execution time at given condition

def pa(n):
    for i in range(0,n):
        if(i%2==0):
            print(i)
        elif(i%2!=0):
            print('this is passed')
            pass

s=int(input('enter n value:'))
pa(s)