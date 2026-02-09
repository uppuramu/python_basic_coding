# get 5 elements from the user an print upper and lower case of each

st=set()
for i in range(0,5):
    n=input('name:')
    st.add(n)
print(st)
for i in st:
    print(i.lower())
    print(i.upper())