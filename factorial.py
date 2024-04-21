num=int(input("Enter the number:"))
if num <0:
    print("INVALID")
elif num ==0:
    print("the value for zero is 1:")
else:
    for i in range(1,num):
        num=num*i
    print(num)