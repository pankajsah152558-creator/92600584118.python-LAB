
# 1. Demonstration of break
print("Break Statement:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# 2. Demonstration of continue
print("\nContinue Statement:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 3. Demonstration of pass
print("\nPass Statement:")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
