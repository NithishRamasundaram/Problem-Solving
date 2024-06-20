n=input("Enter string 1:")
m=input("Enter string 2:")
l=sorted(n)
k=sorted(m)
if l==k:
    print("Two strings are anagram")
else:
    print("Two strings are not anagram")