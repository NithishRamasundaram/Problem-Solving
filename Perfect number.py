n=int(input("Enter the number:"))
divisors=0
for i in range(1,n):
    if n%i == 0:
        divisors=divisors+i

if n == divisors:
    print("Given number is a perfect number")
else:
    print("Given number is not a perfect number")