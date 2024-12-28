n=input("Enter the sentence:")
space=" "
count=0
for i in n:
    if i in space:
        count=count+1
count+=1
print("Number of words in the sentence is:",count)

'''n=input("Enter the sentence:")
count=n.split()
print("Number of words in sentence:",len(count))'''