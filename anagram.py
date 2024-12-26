a=input("Enter string 1:")
b=input("Enter string 2:")
a=a.replace(" ","").lower()
b=b.replace(" ","").lower()
n=sorted(a)
m=sorted(b)
if n==m:
    print("Given strings are anagram")
else:
    print("Given strings are not anagram")