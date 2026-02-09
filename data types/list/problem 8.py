# get 5 numbers from user and store in list
# find square of each element and print

lst=[]
for i in range(1,6):
    n=int(input('number:'))
    lst.append(n)

for i in lst:
    print(i,'square',i*i)
    