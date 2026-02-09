# get two sets and find set difference
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

print(a.difference(b))

