n=int(input("Enter the number:"))
temp=n
rev=0
while(n>0):
    rem = n % 10  # Extract the last digit of the number
    rev = rev * 10 + rem  # Build the reversed number by shifting digits left and adding the last digit
    n = n // 10  # Remove the last digit from the number using integer division
if temp==rev:
    print("The number is palindrome")
else:
    print("The number is not a palindrome")