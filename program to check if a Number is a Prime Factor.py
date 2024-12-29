num=int(input("Enter the number:"))
factor=int(input("Factor of the number:"))
res=1
if num%factor==0:
    for i in range(2,factor):
        if factor%i==0:
            res=0
if res==1:
    print(factor, "is prime factor of", num)
else:
    print(factor, "is not a prime factor of", num)
