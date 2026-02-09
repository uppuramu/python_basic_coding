# get 5 colors and color code from user and print 
# the color and color code in upper case

from re import A


dict={}
for i in range(0,5):
    cod=input('enter color code:')
    col=input('color:')
    dict[cod]=col
print(dict)
for i,j in dict.items():
    print(i.upper()+':'+j.upper()) 