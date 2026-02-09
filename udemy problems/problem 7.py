# find sum and avarage of numbers in string

st=input('enter string:')
sum=0
count=0
for i in st:
    if i.isdigit():
        sum=sum+int(i)
        count=count+1
print('avg:',sum/count)
print(sum)