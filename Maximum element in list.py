n=[5,6,3,9,7,10]
if not n:
    maxi=None
else:
    maxi=n[0]
    for i in n:
        if i > maxi:
            maxi=i
if maxi is not None:
    print("Maximum number is ",maxi)
else:
    print("The list is empty")

'''n=[9,4,5,6,7,0]
print(max(n))'''