
# 1. Tuple Operations
t = (10, 20, 30, 40, 50)

print("Original Tuple:", t)
print("First Element:", t[0])
print("Last Element:", t[-1])
print("Tuple Slicing:", t[1:4])
print("Length of Tuple:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# 2. Set Operations
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("\nSet A:", A)
print("Set B:", B)

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("Difference (A - B):", A - B)

# Symmetric Difference
print("Symmetric Difference:", A ^ B)

# Add and Remove Elements
A.add(50)
print("After Adding 50:", A)

A.remove(20)
print("After Removing 20:", A)
