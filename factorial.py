n=int(input("Enter the number:"))
if n<0:
    print("Invalid")
elif n==0:
    print("The value for zero is 1")
else:
    for i in range(1,n):
        n=n*i
    print(n)