
# Create a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# 1. List Indexing
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# 2. List Slicing
print("First Three Elements:", numbers[0:3])
print("Elements from Index 2:", numbers[2:])
print("Reversed List:", numbers[::-1])

# 3. List Manipulation
numbers.append(60)
print("After Append:", numbers)

numbers.insert(1, 15)
print("After Insert:", numbers)

numbers.remove(30)
print("After Remove:", numbers)

numbers[0] = 5
print("After Updating:", numbers)

# 4. List Comprehension
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", even_numbers)
