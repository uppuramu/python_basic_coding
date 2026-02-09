# 3) get 5 student names and their marks and 
#    print name ,marks

std={}
for i in range(0,5):
    n=input('enter name:')
    m=int(input('enter marks:'))
    std[n]=m
for i,j in std.items():
    print(i,':',j)