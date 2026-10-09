
import random

# Generate a random integer
print("Random Integer:", random.randint(1, 100))

# Generate a random float
print("Random Float:", random.random())

# Generate a random number within a range
print("Random Number:", random.randrange(1, 50, 5))

# Select a random element from a list
numbers = [10, 20, 30, 40, 50]
print("Random Choice:", random.choice(numbers))

# Shuffle a list
random.shuffle(numbers)
print("Shuffled List:", numbers)
