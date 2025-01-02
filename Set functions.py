# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. Add an element
set1.add(10)
print("After add:", set1)

# 2. Update with multiple elements
set1.update([11, 12])
print("After update:", set1)

# 3. Remove an element (raises an error if not found)
set1.remove(10)
print("After remove:", set1)

# 4. Discard an element (does not raise an error)
set1.discard(15)  # No error even if 15 is not in the set
print("After discard:", set1)

# 5. Pop an element (removes and returns a random element)
popped_element = set1.pop()
print("Popped element:", popped_element)
print("After pop:", set1)

# 6. Clear the set
set1.clear()
print("After clear:", set1)

# Reset set1 for further operations
set1 = {1, 2, 3, 4, 5}

# 7. Union
union_set = set1.union(set2)
print("Union:", union_set)

# 8. Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# 9. Difference
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# 10. Symmetric Difference
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)

# 11. Subset check
print("Is set1 a subset of set2?", set1.issubset(set2))

# 12. Superset check
print("Is set1 a superset of {1, 2}?", set1.issuperset({1, 2}))

# 13. Disjoint check
print("Are set1 and set2 disjoint?", set1.isdisjoint({9, 10}))
