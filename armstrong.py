num=int(input("Enter the number:"))
temp=num
rev=0
while temp>0:
    rem=temp%10
    rev=rev+rem**3
    temp//=10
if num==rev:
    print("ARMSTRONG NUMBER")
else:
    print("not a armstrong number")