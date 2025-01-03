n=list(map(int,input("Enter the list:").split(",")))
uniq=[]
for i in n:
    if i not in uniq:
        uniq.append(i)
k=len(uniq)
uniq.sort()
print(k,uniq)