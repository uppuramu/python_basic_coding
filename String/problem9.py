# reverse a geven string




str=input('enter string:')
def reverse(s):
    r_str=''
    for i in str:
        r_str=i+r_str
    print(r_str)

reverse(str)