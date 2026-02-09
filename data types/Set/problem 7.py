# get 2 sets and print all values except duplicate values

from locale import MON_1, MON_12


a=set()
b=set()
print("enter 1st set elements..")
for i in range(5):
    n=int(input("num:"))
    a.add(n)
print("enter 2st set elements..")
for j in range(5):
    m=int(input("num:"))
    b.add(m)
print(a)
print(b)
print(a.symmetric_difference(b))

