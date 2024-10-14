def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_in_range(start, end): 
    for num in range(start, end + 1): #iterate through start and end
        if prime(num):
            print(num,end=" ")

# Input
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Finding and printing prime numbers in the range
print(f"Prime numbers between {start} and {end} are:")
prime_in_range(start, end)
