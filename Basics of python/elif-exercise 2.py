#to read marks and print grade

m=int(input('enter your marks:'))
if(m>90 and m<=100):
    print('A grade')
elif(m>80 and m<=90):
    print('B grade')
elif(m>70 and m<=80):
    print('C grade')
elif(m>60 and m<=70):
    print('D grade')
elif(m>50 and m<=60):
    print('E grade')
else:
    print('fail..')