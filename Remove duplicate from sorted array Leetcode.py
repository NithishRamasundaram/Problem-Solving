n=list(map(int,input("Enter the sorted list:").split(",")))
uniq=[]
for i in n:
    if i not in uniq:
        uniq.append(i)
k=len(uniq)
print(k,uniq)