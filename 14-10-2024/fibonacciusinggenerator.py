def fibonacci(num):
    a, b = 0, 1
    for _ in range(num):
        yield a #The  yield a returns the current Fibonacci number.
        a, b = b, a + b

# Input
num = int(input("Enter the number: "))
print("Fibonacci series:")

# Create the generator
fib_generator = fibonacci(num)

# Using next() to print Fibonacci numbers
for _ in range(num):
    fib_num = next(fib_generator)  # Get the next Fibonacci number
    print(fib_num, end=" ")
