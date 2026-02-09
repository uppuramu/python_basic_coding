# get string and change the any word with new word in given sentence

str=input('enter a string:')
print('old sent:'+str)
old=input('enter old word:')
new=input('enter new word:')
new_s=str.replace(old,new)
print('new sent:'+new_s)