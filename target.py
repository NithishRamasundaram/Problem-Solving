n=int(input("enter number:"))
f=1
if n==0:
    print("factorial is",f)
elif n > 0:
    for i in range(2,n+1):
        f=f*i
print("The factorial is ",f)