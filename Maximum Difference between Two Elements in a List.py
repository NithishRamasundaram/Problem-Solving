n=list(map(int,input("Enter the number:").split(",")))
if len(n) < 0:
    print("Invalid input")
else:
    maxi=max(n)
    mini=min(n)
    difference=maxi-mini
    print("Maximum Difference between Two Elements in a List:",difference)
