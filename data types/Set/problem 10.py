# get set from user and remove one element from set and print 
# and add same element to set and once again print set

a=set()
for i in range(5):
    n=int(input("num:"))
    a.add(n)
print(a)
b=int(input('enter element to remove:'))
a.remove(b)
print(a)
a.add(b)
print(a)