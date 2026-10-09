
# Demonstration of Mutable and Immutable Objects

# 1. Mutable Object (List)
my_list = [10, 20, 30]
print("Original List:", my_list)

my_list[0] = 100
print("Modified List:", my_list)

# 2. Immutable Object (Tuple)
my_tuple = (10, 20, 30)
print("\nOriginal Tuple:", my_tuple)

# Creating a new tuple instead of modifying the original
my_tuple = (100, 20, 30)
print("New Tuple:", my_tuple)

# 3. Immutable Object (String)
my_string = "Hello"
print("\nOriginal String:", my_string)

my_string = "Python"
print("New String:", my_string)
