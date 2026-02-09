# write a code to read a sentence from user and find total number of characters
# and covert upper case and
# place dot and end of sentence

sen=input('enter a sentence:')
n=len(sen)
print('no of characters:',n)
if sen.isupper():
    print('it is uppercase')
    print(sen+'.')
else:
    print('converted to upper case')
    print(sen.upper()+'.')