# print min ,max value from dictionary

dict={
    1:10,
    2:7,
    3:8,
    4:20,
    5:44
    }
lst=[]
for i in dict.values():
    lst.append(i)
print(min(lst))
print(max(lst))

# or..or..or..or..or..or
print(min(dict.values()))
print(max(dict.values()))