n=int(input("Enter the number:"))
count=0
while(n>0):
    digit=n%10
    count=count+digit
    n=n//10
print(count)

'''
n=int(input("Enter the number:"))
m=str(n)
count=0
for i in m:
    count=count+int(i)
print(count)'''