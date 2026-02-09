# create tuple with name and search any name in list

tup=('a','b','c','d','e')
n=input("enter name:")
for i in tup:
    if n==i:
        print('your name is available')