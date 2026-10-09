
# Demonstration of string operations

s = "Hello Python"

# 1. String Slicing
print("Original String:", s)
print("First five characters:", s[0:5])
print("First character:", s[0])
print("Last character:", s[-1])
print("Reverse String:", s[::-1])

# 2. String Formatting
name = "Rahul"
age = 18
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

# 3. Built-in String Functions
text = "  hello python  "
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalized:", text.capitalize())
print("Length:", len(text))
print("Replace:", text.replace("python", "world"))
print("Stripped:", text.strip())
print("Count of 'o':", text.count("o"))
print("Find 'python':", text.find("python"))
