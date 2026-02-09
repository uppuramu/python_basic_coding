#  code for get 5 items from the user and remove the first item and print
lst=[]
for i in range(1,5):
    n=input('enater a name:')
    lst.append(n)
lst.pop(0)
print(lst)