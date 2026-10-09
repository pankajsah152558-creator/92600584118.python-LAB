
# 1. Positional Arguments
def add(a, b):
    print("Addition:", a + b)

add(10, 20)

# 2. Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=18, name="Rahul")

# 3. Default Arguments
def greet(name="Student"):
    print("Hello,", name)

greet()
greet("Rahul")

# 4. Variable-Length Arguments (*args)
def total(*numbers):
    print("Total:", sum(numbers))

total(10, 20, 30, 40)

# 5. Variable-Length Keyword Arguments (**kwargs)
def display(**details):
    for key, value in details.items():
        print(key, ":", value)

display(name="Rahul", course="Python", age=18)
