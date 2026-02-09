#read 5 five names of user and print names starts with letter " A or a"
list=[]
for i in range(0,5):
    name=input('enter name:')
    list.append(name)
for i in list:
    if i.startswith("a" or "A"):
        print(i)