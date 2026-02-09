# read 5 numbers from user and find minimum number
list=[]
for i in range(0,6):
    n=int(input('enter a number:'))
    list.append(n)
mi=min(list)
print(mi)
