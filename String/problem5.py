# to get name from user and it star with 'a' then print
# otherwise error 

str=input('enter name:')
if str.startswith('a'):
    print(str+'\t starts with A')
else:
    print('wrong')