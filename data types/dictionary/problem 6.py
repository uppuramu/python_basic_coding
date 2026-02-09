# create diction with numaric items
# print the keys which having even values

dict={1:22,2:33,3:44,4:55,5:66}
for i,j in dict.items():
    if j%2==0:
        print(i)