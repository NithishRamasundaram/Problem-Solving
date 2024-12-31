# Sample list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 1. Append
fruits.append("fig")
print("1. Append 'fig':", fruits)

# 2. Extend
fruits.extend(["grape", "honeydew"])
print("2. Extend with ['grape', 'honeydew']:", fruits)

# 3. Insert
fruits.insert(2, "blueberry")
print("3. Insert 'blueberry' at index 2:", fruits)

# 4. Remove
fruits.remove("banana")
print("4. Remove 'banana':", fruits)

# 5. Pop
popped_item = fruits.pop()
print("5. Pop the last item:", popped_item, "| Remaining list:", fruits)

# 6. Index
print("6. Index of 'cherry':", fruits.index("cherry"))

# 7. Count
fruits.append("apple")
print("7. Count of 'apple':", fruits.count("apple"))

# 8. Sort
fruits.sort()
print("8. Sort the list:", fruits)

# 9. Reverse
fruits.reverse()
print("9. Reverse the list:", fruits)

# 10. Copy
fruits_copy = fruits.copy()
print("10. Copy of the list:", fruits_copy)

# 11. Clear
fruits_copy.clear()
print("11. Clear the copied list:", fruits_copy)

# 12. Length
print("12. Length of the list:", len(fruits))

# 13. List slicing
print("13. Slicing [1:4]:", fruits[1:4])

# 14. Check existence
print("14. Check if 'apple' exists:", "apple" in fruits)

# 15. Iterate through the list
print("15. Iterate through the list:")
for fruit in fruits:
    print("-", fruit)

# 16. List comprehension
squared_numbers = [x**2 for x in range(5)]
print("16. List comprehension (squares of 0-4):", squared_numbers)

# 17. Nested lists
nested_list = [["a", "b", "c"], [1, 2, 3], [True, False]]
print("17. Nested list:", nested_list)
print("Access element [1][2]:", nested_list[1][2])

# 18. Joining lists
more_fruits = ["kiwi", "lemon"]
combined_list = fruits + more_fruits
print("18. Joining lists:", combined_list)

# 19. Multiplying lists
print("19. Multiplying list by 2:", more_fruits * 2)

# 20. Deleting an element
del fruits[2]
print("20. Delete element at index 2:", fruits)
