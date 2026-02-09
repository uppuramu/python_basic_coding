#to get 5 user nemes and store in list display all students names 
# with upper case letters

list=[]
for i in range(0,6):
    name=input('enter neme:')
    list.append(name)
for i in list:
    print(i.upper())