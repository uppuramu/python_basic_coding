import random
list=['rock','paper','scissor']
com=random.choice(list)

def rps():
    sel=int(input('select any one from these:\n1)rock\n2)paper\n3)scissor:'))
    if(sel==1):
        aaa='rock'
    elif(sel==2):
        aaa='paper'
    elif(sel==3):
        aaa='scissor'
    else:
        print('wrong input.....')
    return aaa  

def checking(a,b):
    if(a==b):
        print('Tie')
    elif(a=='scissor'and b=='paper' or b=='scissor'and a=='paper'):
        if(a=='scissor'):
            print('computer win...\ntry again to win')
        else:
            print('user win...')
    elif(a=='rock'and b=='paper' or b=='rock'and a=='paper'):
        if(a=='paper'):
            print('computer win...\ntry again to win')
        else:
            print('user win...')
    elif(a=='scissor'and b=='rock' or b=='scissor'and a=='rock'):
        if(a=='rock'):
            print('computer win...\ntry again to win')
        else:
            print('user win...')

user=rps()
print('computer chooice is:'+com)
print(' user    chooice is:'+user)
checking(com,user)

