# to print odd number from 50 to 1
#and find their sum

sum=0
for i in range(50,0,-1):
    if(i%2!=0):
        print(i)
        sum=sum+i
print('sum is:',sum)