# create list with colors and find specific color count by usind functions


lst=['red','white','green','orange','red','white','pink','red','white','green','orange','red','white']


def color(a,n):
    count=0
    for i in a:
        if i==n:
            count=count+1
    print(n,':',count)

c=input('enter color name to count:')
color(lst,c)