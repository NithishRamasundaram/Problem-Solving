num=int(input("Enter the number"))
if num>1:
    for i in range(2,num):
        if(num%i==0):
            k=0
        else:
            k=1

if k==0:
    print("Non prime")
else:
    print(("Prime number"))