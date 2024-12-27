n=int(input("Enter the number:"))
prime=1
if n>1:
    for i in range(2,n):
        if n%i!=0:
            pass
        else:
            prime=0
if prime==1:
    print("Given number is prime")
else:
    print("Given number is not a prime")