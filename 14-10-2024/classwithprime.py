class PrimeandFib:
    def prime(self, num):
        if num < 2:
            return False
        for i in range(2, num):  # Check for factors from 2 to num-1
            if num % i == 0:
                return False
        return True

    def prime_in_range(self, start, end): 
        primes = []  #  to store prime numbers
        for num in range(start, end + 1):  # Iterate through start and end
            if self.prime(num):
                primes.append(num)  # Append prime number to the list
        return primes  # Return the list of prime numbers
    
    def fibonacci(self, number):
        a, b = 0, 1
        fibo_sequence = []  # List to store Fibonacci numbers
        for _ in range(number):
            fibo_sequence.append(a)  # Append current Fibonacci number
            a, b = b, a + b
        return fibo_sequence  # Return the list of Fibonacci numbers

# Input for Fibonacci series
number = int(input("Enter the number for Fibonacci series: "))

# Input for prime numbers
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Create an instance of the PrimeandFib class
prime_and_fib_obj = PrimeandFib()

# Get Fibonacci series and prime numbers
fibo_series = prime_and_fib_obj.fibonacci(number)
prime_numbers = prime_and_fib_obj.prime_in_range(start, end)

# Print the results
print("Fibonacci Series:", ', '.join(map(str, fibo_series)))
print("Prime Numbers:", ', '.join(map(str, prime_numbers)))
