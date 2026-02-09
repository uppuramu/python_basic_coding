# get 5 student name from user store in tuple
# print in upper case



lst=[]
for i in range(0,5):
    i=input('name:')
    lst.append(i)
tup=tuple(lst)
# list to tuple convertion
print(type(tup))

for i in tup:
    print(i.upper())