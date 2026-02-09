# get 5 names and print names start with r


lst=[]
for i in range(5):
    lst.append(input('enter name:'))

lst.sort()
print(lst)
for i in lst:
    if i.startswith('r'):
        print(i)