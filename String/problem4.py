# to accept only numbers otherwise print it contain characters and special symbols

str=input('enter string of only numers:')

if(str.isnumeric()):
    print('given input is only numbers\n'+str)
else:
    print(str+'\tdoes not contain only numbers')