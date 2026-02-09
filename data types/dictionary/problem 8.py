# to chect whether a specific key is exits or not

dict={
    1:10,
    2:7,
    3:8,
    4:20,
    5:44
    }
key=int(input('enter key value to check:'))
for i in dict.keys():
    if i==key:
        print('exits..........')
     