# get two sets and find which is the superset .

a=set()
b=set()
c=int(input('enter length of set a:'))
for i in range(c):
    e=int(input('enter ele:'))
    a.add(e)
d=int(input('enter length of set b:'))
for i in range(d):
    n=int(input('enter ele:'))
    b.add(n)
print(a)
print(b)
if a.issubset(b):
    print("a is sub set of b")
elif b.issubset(a):
    print('b is subset of a')
    
    
    