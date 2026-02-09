#list is mutable data type.
#update or change the each value.
# denoted by ' [ ] '
#list  works like a array

lst=[1,2,3,4,5,6,'ramu']
print(lst)
print(type(lst))

print(lst[4])
print(lst[-1])

lst[5]=7
print(lst)

for i in lst:
    print(i)

print(3 in lst)

print(7 not in lst)


