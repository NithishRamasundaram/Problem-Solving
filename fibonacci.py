n=int(input("Enter Fibo series number:"))
a=0
b=1
print(a,b,end=" ")
for i in range(2,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

'''
n=int(input("Enter the number:"))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
'''