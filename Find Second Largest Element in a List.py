n=list(map(int,input("Enter the list:").split(",")))
f_max=max(n)
n.remove(f_max)
s_max=max(n)
print("Second Largest Element in a List:",s_max)