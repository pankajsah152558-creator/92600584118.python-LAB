
# 1. Demonstration of if statement
num = 10

if num > 0:
    print("Number is positive")

# 2. Demonstration of if-else statement
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# 3. Demonstration of if-elif-else statement
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade F")
