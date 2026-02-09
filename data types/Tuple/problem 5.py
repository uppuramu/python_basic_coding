# crete tuple with 10 values and
# find their sum and multiplication  and print 
tup=(1,2,3,4,5,6,7,8,9,10)
sum=0
mul=1
for i in tup:
    sum=sum+i

for i in tup:
    mul=mul*i

print(sum)
print(mul)