# user delete an element from list

lst=['a','c','b','A','B','C','D']
c=input('del ele:')
for i in lst:
    if i==c:
        lst.remove(i)
        #   or
        #a=lst.index(c)
        #lst.pop(a)
print(lst)