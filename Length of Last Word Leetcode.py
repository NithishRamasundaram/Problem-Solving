n=input("Enter the string:")
n=n[::-1]
last=""
for i in n:
    if i ==" ":
        break
    last=last+i
l=len(last)
print("The length of the last word is:",l)

