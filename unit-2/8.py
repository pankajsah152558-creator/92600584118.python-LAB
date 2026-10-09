
# Global variable
x = 10

def outer():
    # Nonlocal variable
    y = 20

    def inner():
        # Local variable
        z = 30
        nonlocal y
        global x

        y = y + 5
        x = x + 5

        print("Local variable z:", z)
        print("Nonlocal variable y:", y)
        print("Global variable x:", x)

    inner()
    print("Value of y in outer():", y)

outer()
print("Value of x outside function:", x)
