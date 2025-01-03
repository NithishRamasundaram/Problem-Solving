n=list(map(int,input("Enter the sorted array:").split(",")))
uniq=[]
for i in n:
    if uniq.count(i)<2:
        uniq.append(i)
k=len(uniq)
print(k,uniq)
