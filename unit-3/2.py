
# 1. Import entire module
import math
print("Square root:", math.sqrt(25))

# 2. Import specific function
from math import factorial
print("Factorial:", factorial(5))

# 3. Import with an alias
import math as m
print("Value of pi:", m.pi)

# 4. Import multiple functions
from math import ceil, floor
print("Ceiling:", ceil(4.3))
print("Floor:", floor(4.8))

# 5. Import all names from a module
from math import *
print("Power:", pow(2, 3))
