# write a code to read a name and print,it contain above 4 letters and below 10 letters
# ana startwith 'a' letter
name=input('enter your name:')
if(len(name)==5 or len(name)<10):
    if(name.startswith('a')):
        print('your name is '+name)
    else:
        print('not valid')
else:
        print('not valid')