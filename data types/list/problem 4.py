# read 10 numbers and print tnhe numbers which lessthan 20 and greater than 10
list=[]
for i in range(0,11):
    num=int(input('enter number:'))
    list.append(num)
for i in list:
    if(i>10 and i<20):
        print(i)