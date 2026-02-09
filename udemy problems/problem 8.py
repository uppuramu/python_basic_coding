# create even,odd list and find sum and 
# multiplication each number and print
esum=0
emul=1
even=[i for i in range(1,101) if i%2==0 ]
print(even)
for i in even:
    esum=esum+i
    emul=emul*i
print(esum)
print(emul)
osum=0
omul=1
odd=[i for i in range(0,1) if i%2!=0]
print(odd)
for i in odd:
    osum=osum+i
    omul=omul*i
print(osum)
print(omul)