# get 5 names and print names with size 5 letters

lst=[]
for i in range(5):
    lst.append(input('enter name:'))

lst.sort()
print(lst)
for i in lst:
    if len(i)==5:
        print(i)