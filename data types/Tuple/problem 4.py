# get 10 number and store in tuple
# print number divisible by 2 and 3

lst=[]
for i in range(0,10):
    i=int(input('num:'))
    lst.append(i)
tup=tuple(lst)


for i in tup:
    if i%2==0 and i%3==0:
        print(i)