# get 5 elemnts and store in list and then add they into set

lst=[]
a=set()
for i in range(5):
    n=int(input('enter ele:'))
    lst.append(n)
for j in lst:
    a.add(j)
print(lst)
print(a)

### orrrr

print(set(lst))