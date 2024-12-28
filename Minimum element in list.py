n=[5,6,3,9,7,10]
if not n:
    mini=None
else:
    mini=n[0]
    for i in n:
        if i < mini:
            mini=i
if mini is not None:
    print("Minimum number is",mini)
else:
    print("The list is empty")

'''n=[9,4,5,6,7,0]
print(min(n))'''