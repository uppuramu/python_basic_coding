# find the count od character with space 
# and with out space
# input given by the user
str=input("enter sentance:")
wsc=0
wosc=0
wsc=len(str)
print(wsc)
for i in str:
    if i.isalpha():
        wosc=wosc+1
print(wosc)

