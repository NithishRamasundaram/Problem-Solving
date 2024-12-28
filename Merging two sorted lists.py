a = [1, 3, 5, 7]
b = [2, 4, 6, 9]
a.extend(b)
s = sorted(a)
print("Merged list:", s)

'''Not efficient for already sorted input lists since it doesn't take advantage of their sorted property.'''