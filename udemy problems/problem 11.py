# create function pass list with size 10 and fins min max element

lst=[]
for i in range(0,10):
    n=int(input('enter number:'))
    lst.append(n)

def minmax(a):
    print(min(a))
    print(max(a))

minmax(lst)