#  get 5 word from user
# display the words ends with  ' n '
lst=[]
for i in range(0,5):
    i=input('word:')
    lst.append(i)
tup=tuple(lst)

for i in tup:
    if i.endswith('n'):
        print(i)