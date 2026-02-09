# get two sets and find intersection 

a=set()
b=set()
for i in range(5):
    e=int(input('enter ele:'))
    a.add(e)
for i in range(5):
    n=int(input('enter ele:'))
    b.add(n)
print(a)
print(b)
print(a.intersection(b))   