# get 5 numbers from user and find sum and product of that numbers 

st=set()
for i in range(5):
    n=int(input("enter number:"))
    st.add(n)
print(st)
sum=0
pro=1
for i in st:
    sum=sum+i
    pro=pro*i
print(sum)
print(pro)