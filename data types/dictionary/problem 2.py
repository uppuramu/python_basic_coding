#2) get 5 number from user and find the square of number 
# and plced in dictionary and print

dict={}
for i in range(0,5):
    n=int(input('num:'))
    dict[n]=n*n
print(dict)