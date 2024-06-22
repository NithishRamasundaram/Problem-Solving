num=int(input("enter the number:"))
count=0
n1=0
n2=1
while count < num:
    print(n1)
    c=n1+n2
    n1=n2
    n2=c
    count+=1