n=int(input("Enter Amstrong number:"))
temp=n
rev=0
while n > 0:                        # Loop runs until `temp` becomes 0.
    rem = n % 10                    # Get the last digit of the number.
    rev = rev + rem**3              # Add the cube of the last digit to `rev`.
    n //= 10                        # Remove the last digit from `temp` by performing integer division.
if temp==rev:
    print("Given number is Amstrong number")
else:
    print("Giver number is not an Amstrong number")