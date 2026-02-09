# to print gratest of 3 number by using function

from codecs import oem_decode


def great(x,y,z):
    if(x>y and x>z):
        print('big no is:',x)
    elif(y>x and y>z):
        print('big no is:',y)
    else:
        print('big no is:',z)
           
m=int(input('enter 1st no:'))
n=int(input('enter 2nd no:'))
o=int(input('enter 3rd no:'))

great(m,n,o)