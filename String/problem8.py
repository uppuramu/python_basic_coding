# to get no. from user and print numbers from 1 to given input
# and find their sum and print

n=int(input('enter number:'))
sum=0
for i in range(1,n+1):
    print(i)
    sum=sum+i
print('sum is:',sum)