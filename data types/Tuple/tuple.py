#  tuple is a data type and immutable(can't change tuplle elements after creation a tuple)
#  tuple works like list but some diffrence
#  denoted by  ' ( ) '
# tuple contain diffrent data types
#  it is order data strcture and stored in sequence
# we create tuple inside the another tuple
# we can add tuples(tup+tup)
# we can't change tuple items (get error)

from xml.sax.handler import DTDHandler


tup1=('a','b','c')
print(type(tup1))
tup2=(1,2,3)
print(type(tup2))
tup=tup1+tup2
print(tup)

print('a' in tup1)
print(1 in tup2)

# tup[6]='DDD' ---in this way we can't add items to tuple

for i in tup1:
    print(i)