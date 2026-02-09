# when we use if statement in another if statement.

#ex:- check a number is divisible by 2 and 3
n=int(input('enter a number:'))
if(n%2==0):
    if(n%3==0):
        print('divisible by 2 and 3')
    else:
        print('not divisible')
else:
    print('not divisible')