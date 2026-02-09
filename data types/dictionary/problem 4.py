# 4) get 5 product names and prices and 
#   find the total sum of products

product={}
sum=0
for i in range(0,5):
    n=input('enter name:')
    m=int(input('enter marks:'))
    product[n]=m
for i in product.values():
    sum=sum+i
print('total sum:',sum)
    