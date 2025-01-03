nums=list(map(int,input("Enter the list:").split(",")))
val=int(input("Enter the value to be removed:"))
k=[]
for i in nums:
    if i != val:
        k.append(i)
l=len(k)
print(l,k)