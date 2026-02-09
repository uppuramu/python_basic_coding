# to read 10 numbers into list and print odd numbers in the list
list=[]
for i in range(0,11):
    num=int(input('enter number:'))
    list.append(num)
for i in list:
    if(i%2!=0):
        print(i)