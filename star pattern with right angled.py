n=int(input("Enter the number of stars:"))
for i in range(1,n+1):
    print(" " *(n-i) + "*"* i)