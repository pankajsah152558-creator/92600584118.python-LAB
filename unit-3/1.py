
# mymodule.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
  
# main.py

import mymodule

x = 10
y = 5

print("Addition =", mymodule.add(x, y))
print("Multiplication =", mymodule.multiply(x, y))
