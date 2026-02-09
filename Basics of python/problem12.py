# display odd numbers from 1 - 20
# display even numbers from 20-1
# add both even and odd numbers and add final result of each

i=1
esum=0
osum=0
while(i<=20):
    if(i%2==0):
        esum=esum+i
    i=i+1

a=20
while(a>=1):
    if(a%2!=0):
        osum=osum+a
    a=a-1

print('even sum:',esum)
print('odd sum:',osum)