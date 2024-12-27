a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))
if a<b and a<c:
    print("1st number is smaller")
elif b<a and b<c:
    print("2nd number is smaller")
else:
    print("3rd number is smaller")