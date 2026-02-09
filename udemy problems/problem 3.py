# create dictionary with given dictionary as key valus and their squares

dict={1:'a',2:'b',3:'c',4:'d',5:'e'}
dictnew={}
for i in dict.keys():
    dictnew[i]=i*i
print(dictnew)