n=int(input("Enter the number:"))
n=str(n)
h=n[::-1]
if n==h:
    print("The number is palindrome")
else:
    print("The number is not a palindrome")