'''n=int(input("Enter Factorial number:"))
if n<0:
    print("Invalid input")
elif n==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,n):
        n=n*i
    print(n)'''

num=int(input("Enter Factorial number:"))
if num<0:
    print("Invalid input")
elif num==1:
    print("Factorial value of 0 is 1")
else:
    n=1
    for i in range(1,num+1):
        n=n*i
    print(n)