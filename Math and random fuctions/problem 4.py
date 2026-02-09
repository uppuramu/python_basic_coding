# read 5 numbers from user and find maximum number
list=[]
for i in range(0,6):
    n=int(input('enter a number:'))
    list.append(n)
ma=max(list)
print(ma)