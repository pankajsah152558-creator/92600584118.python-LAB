
# Demonstration of Iterables and Iterators

# Create an iterable
numbers = [10, 20, 30, 40, 50]

print("Iterable:", numbers)

# Create an iterator
it = iter(numbers)

print("\nIterator Elements:")
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Using iterator with a loop
print("\nUsing Iterator with Loop:")
it = iter(numbers)

for item in it:
    print(item)
