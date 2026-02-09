# get 10 number and store in tuple
# print odd numbers

lst=[]
for i in range(0,10):
    i=int(input('num:'))
    lst.append(i)
tup=tuple(lst)
# list to tuple convertion
print(type(tup))

for i in tup:
    if i%2!=0:
        print(i)