n=input("Enter the string:")
unique=""
for i in n:
    if i not in unique:
        unique=unique+i
print(unique)