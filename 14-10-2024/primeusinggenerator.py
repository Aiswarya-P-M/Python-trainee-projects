def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
# This function is a generator that yields prime numbers within a specified range
def generate_primes_in_range(start, end): 
    for num in range(start, end + 1):
        if prime(num):
            yield num

# Input
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Finding and generating prime numbers in the range
prime_gen = generate_primes_in_range(start, end)

print(f"Prime numbers between {start} and {end} are:")
while True: #This while loop manually retrieves prime numbers from the generator using next()
    prime_num = next(prime_gen, None)  # next(prime_gen, None) fetches the next prime number from the generator. If the generator is exhausted (i.e., no more primes to yield), it returns None as the default value.
    if prime_num is None:
        break
    print(prime_num, end=" ")

