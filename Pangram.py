s=input("Enter the string:")
s=s.replace(" ","")
s=s.lower()
n=set(s)
m=len(n)
if m==26:
    print("Given string is Pangram")
else:
    print("Given string is not pangram")