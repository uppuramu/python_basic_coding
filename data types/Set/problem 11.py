# get names in to set and pprint their length
a=set()
count=1
for i in range(5):
    n=input("num:")
    a.add(n)
for i in a:
    print(i,len(i))