#  write a code for to check two objects are same or not
#   and check object is present in given list

a=int(input('a='))
b=int(input('b='))
if(a is b):
    print('same')
else:
    print('not same')

list=['red','black','green','orange']
r=input('enter color:')
for i in list:
    if(i==r):
        print('same'+i)
    else:
        print('not in')