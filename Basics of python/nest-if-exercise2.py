#read age and marks
#age>=18
# 90<marks<100
# select that users

age=int(input('enter age:'))
marks=int(input('enter marks:'))
if(age>=18):
    if(marks>90 or marks<100):
        print('you are selected..')
    else:
        print('marks issue')
else:
        print('age issue')