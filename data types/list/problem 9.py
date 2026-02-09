# get 5 any words from user and display the word ends with --'n'
lst=[]
for i in range(1,6):
    n=input('word:')
    lst.append(n)
print('requred names..')
for i in lst:
    if i.endswith('n'):
        print(i)