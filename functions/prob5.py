# get the username it contain only alpha numaric values
# and length is 8 or <20

def usr(u):
    if (u.isalnum() and len(u)>=8 and len(u)<=15):
        print('user is valid:\t'+u)
    else:
        print('user name is not valid:')

s=input('enter username:')
usr(s)