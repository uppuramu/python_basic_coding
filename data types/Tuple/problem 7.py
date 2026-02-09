# create tuple with 10 items and
# print numbers divisible by 2 and 3
tup=(2,3,4,5,6,7,8,9,12,18)
for i in tup:
    if i%2==0 and i%3==0:
        print(i)