# Sample string
text = "Hello, Python is fun! Practice makes Perfect."

# String length
print("1. Length of the string:", len(text))

# Case conversion
print("2. Uppercase:", text.upper())
print("3. Lowercase:", text.lower())
print("4. Title case:", text.title())
print("5. Swap case:", text.swapcase())
print("6. Capitalize first letter:", text.capitalize())

# Searching and finding
print("7. Find 'Python':", text.find('Python'))
print("8. Count of 'e':", text.count('e'))
print("9. Starts with 'Hello':", text.startswith('Hello'))
print("10. Ends with 'Perfect.':", text.endswith('Perfect.'))

# Replace and strip
print("11. Replace 'fun' with 'awesome':", text.replace('fun', 'awesome'))
whitespace_text = "   Extra spaces!   "
print("12. Strip whitespace:", whitespace_text.strip())
print("13. Left Strip:", whitespace_text.lstrip())
print("14. Right Strip:", whitespace_text.rstrip())

# Splitting and joining
print("15. Split into words:", text.split())
print("16. Join with '-':", '-'.join(['Join', 'with', 'hyphen']))

# Alignment
print("17. Centered string:", text.center(50, '*'))
print("18. Left-aligned:", text.ljust(50, '-'))
print("19. Right-aligned:", text.rjust(50, '-'))

# Check string properties
print("20. Is alphanumeric:", "Python123".isalnum())
print("21. Is alphabetic:", "Python".isalpha())
print("22. Is digit:", "12345".isdigit())
print("23. Is lowercase:", text.islower())
print("24. Is uppercase:", text.isupper())
print("25. Is title case:", text.istitle())

# Encoding and decoding
encoded = text.encode('utf-8')
print("26. Encoded string:", encoded)
print("27. Decoded string:", encoded.decode('utf-8'))

# Partition and rpartition
print("28. Partition on 'Python':", text.partition('Python'))
print("29. rPartition on 'Python':", text.rpartition('Python'))

# Zfill (zero-filling)
num = "42"
print("30. Zero-filled:", num.zfill(5))

# Expanding tabs
tabbed_string = "Hello\tWorld"
print("31. Expanded tabs:", tabbed_string.expandtabs(4))
