
# Create a dictionary
student = {
    "name": "Rahul",
    "age": 18,
    "course": "Python",
    "marks": 85
}

print("Original Dictionary:", student)

# Access dictionary values
print("Student Name:", student["name"])

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Add and update elements
student["city"] = "Rajkot"
student["marks"] = 90
print("After Adding and Updating:", student)

# Remove an element
student.pop("age")
print("After Removing Age:", student)

# Iterate through dictionary
print("\nDictionary Iteration:")
for key, value in student.items():
    print(key, ":", value)

# Check whether a key exists
print("\nIs 'name' present?", "name" in student)

# Dictionary length
print("Dictionary Length:", len(student))
