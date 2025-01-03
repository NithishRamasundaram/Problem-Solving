'''n=input("Enter the string:")
r=input("Occurrence:")
ind=n.index(r)
print("The index of",r,"is",ind)'''

n = input("Enter the string: ")
r = input("Occurrence: ")
needle_len = len(r)

# Loop through the string by index
for i in range(len(n) - needle_len + 1):
    if n[i:i + needle_len] == r:
        print("The index of", r, "is", i)
        break
else:
    # If no match is found, print -1
    print("The index of", r, "is -1")

