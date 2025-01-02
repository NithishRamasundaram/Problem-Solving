# Create a dictionary
my_dict = {'name': 'John', 'age': 30, 'job': 'Engineer'}

# 1. Using clear()
print("Before clear:", my_dict)
my_dict.clear()
print("After clear:", my_dict)

# 2. Using copy()
my_dict = {'name': 'Alice', 'age': 25, 'job': 'Doctor'}
copy_dict = my_dict.copy()
print("Original Dictionary:", my_dict)
print("Copied Dictionary:", copy_dict)

# 3. Using fromkeys()
keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print("New Dictionary with fromkeys:", new_dict)

# 4. Using get()
job = my_dict.get('job', 'Not Available')
print("Job:", job)

# 5. Using items()
items = my_dict.items()
print("Items:", items)

# 6. Using keys()
keys = my_dict.keys()
print("Keys:", keys)

# 7. Using pop()
removed_value = my_dict.pop('age', 'Key not found')
print("Removed Value:", removed_value)
print("Dictionary after pop:", my_dict)

# 8. Using popitem()
key_value = my_dict.popitem()
print("Popped Item:", key_value)
print("Dictionary after popitem:", my_dict)

# 9. Using setdefault()
occupation = my_dict.setdefault('job', 'Engineer')
print("Job (setdefault):", occupation)
print("Dictionary after setdefault:", my_dict)

# 10. Using update()
new_info = {'age': 28, 'city': 'New York'}
my_dict.update(new_info)
print("Dictionary after update:", my_dict)

# 11. Using values()
values = my_dict.values()
print("Values:", values)
