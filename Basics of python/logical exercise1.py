# to check valid user name and password and username and password correct or not

username='ramu'
password=1234
name=input('enter name:')
pwd=int(input('enter password:'))

if(username==name and password==pwd):
    print('log in success fuly....')
else:
    print('faild...')