# to read a sentence and print odd index characters

sen=input('enter sentence:')
total=len(sen)

for i in range(0,total):
    if i%2==0:
        print(sen[i])