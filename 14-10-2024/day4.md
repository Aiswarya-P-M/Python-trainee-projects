# **Training on 14-10-2024**

## **1. Prime Number**

A prime number is a natural number greater than 1 that has no divisors other than 1 and itself. Here we need to finds and prints all the prime numbers within a specified range of integers.

### **Code**

```python
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
```

### **Logic Breakdown** ###

*1. Prime Check Function (prime(num)):*

A function that takes a number num as input and checks whether it is a prime number.
If num is less than 2, the function returns False because prime numbers must be 2 or greater.
It then checks for divisibility by any integer between 2 and num-1. If any divisor is found, the function returns False, indicating that the number is not prime.
If no divisors are found, the function returns True, indicating the number is prime.

*2. Range Function (prime_in_range(start, end)):*

This function takes two arguments, start and end, which define the range within which we want to find prime numbers.
It iterates through all the numbers in the given range (from start to end inclusive) and calls the prime() function for each number.
If a number is found to be prime, it is printed on the same line, separated by a space.

*3. User Input:*

The user is prompted to input the starting and ending values of the range.
The program then displays all prime numbers between these two values using the logic explained above.

## **2. Generators in Python** ###

A generator is a special type of iterable in Python that allows you to iterate over a sequence of values lazily—i.e., it generates values one at a time as needed rather than generating all the values at once. This makes generators memory efficient, especially for large datasets, because they do not store the entire sequence in memory at once.

## **Key points**

1. Lazy Evaluation: Values are generated on the fly, which helps in handling large data.

2. Memory Efficiency: Since values are produced only when needed, memory consumption is low compared to other iterables like lists.

3. Iteration: Generators can be iterated using a loop, like lists or tuples, but they don't support indexing or slicing.

## *Syntax*

Generators are typically created in two ways:

***Generator Function***: A function that uses the yield keyword.

***Generator Expression***: Similar to a list comprehension but with parentheses instead of square brackets.

***Generator Function Syntax***
```python
def generator_function():
    yield value
```
* yield: The yield keyword pauses the function and returns a value. When the function is called again, it resumes where it left off.

***Generator Expression Syntax***
```python
generator_expression = (expression for item in iterable)
``` 

**Example**
```python
# Generator function to yield numbers in a given range
def my_generator(n):
    for i in range(n):
        yield i

# Using the generator
gen = my_generator(5)  # Create a generator that yields numbers from 0 to 4

for num in gen:
    print(num)
```

*Explanation*

1. my_generator(n): 

* This is a generator function that yields numbers from 0 to n-1.
   
* It uses a for loop to iterate through numbers in the range(n).

* Instead of returning values all at once, it yields each value one by one.

2. Using the generator:

* The generator is invoked by assigning it to gen. However, it does not immediately execute the function.
  
* When iterated over using a for loop, it produces the numbers one at a time and prints them.

***Output***
```python
0
1
2
3
4
```

# **3. Prime Number using generators**
```python
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
```

This program generates and prints all the prime numbers within a specified range using a generator function. The generator lazily yields one prime number at a time from the range, and the while loop manually retrieves these numbers using the next() function until the generator is exhausted.

### **Logic Breakdown**

1. Prime Check Function (prime(num)):

* This function checks whether a number is prime.

* If the number is less than 2, it returns False since prime numbers are greater than 1.

* It checks divisibility from 2 up to num-1. If a divisor is found, it returns False, otherwise True.

2. Prime Number Generator (generate_primes_in_range(start, end)):

* This is a generator function that iterates through numbers in the range from start to end.

* For each number, it calls the prime() function to check if it's prime.

* If the number is prime, it is yielded using the yield statement.

* This makes the function return one prime number at a time, on-demand, rather than all at once.

3. Retrieving and Printing Prime Numbers:

* The user inputs the start and end of the range.
The generate_primes_in_range() function is called to create a generator, and the prime_gen variable holds this generator.

* The while loop uses next(prime_gen, None) to manually retrieve the next prime number from the generator.

* The next() function returns the next value in the sequence. If the generator has no more values to yield, it returns None.

* The loop breaks when None is returned, signaling that all primes have been generated and printed.

# **4. Fibonacci Series using generators**

The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1. The first few numbers in the Fibonacci sequence are: 0, 1, 1, 2, 3, 5, 8, 13, and so on. 

### ***Code***

```python 
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
```

### **Logic Breakdown**

1. Fibonacci Generator Function (fibonacci(num)):

* The function initializes two variables, a and b, to 0 and 1, which are the first two numbers in the Fibonacci series.

* It then iterates num times (the number of Fibonacci numbers the user wants).

* In each iteration, it yields the current Fibonacci number (a), and updates a and b to the next two numbers in the sequence (b becomes the new a, and a + b becomes the new b).

2. Input and Setup:

* The user is prompted to input the number of Fibonacci numbers to generate.

* The generator function fibonacci() is called, which returns a generator object that yields Fibonacci numbers one by one.

3. Using the Generator:

* A for loop runs for num iterations, using next(fib_generator) to get the next Fibonacci number from the generator.

* Each Fibonacci number is printed on the same line, separated by a space.

# **5. Classes In Python**

In Python, a class is a blueprint for creating objects. An object is an instance of a class, encapsulating data (attributes) and behavior (methods). Classes help organize code by grouping data and functions related to a specific concept or entity, making it easier to model real-world entities.

Key Concepts:

1. Class: Defines a new type, including attributes (variables) and methods (functions) that belong to the class.
 
2. Object: A specific instance of a class, created using the class constructor.
 
3. Attributes: Variables that store data specific to the object.
 
4. Methods: Functions that define behavior or actions for objects of the class.
   
5. Constructor: A special method (__init__()) that is called when an object is created. It initializes the attributes of the object.
   
### ***Syntax***

```python 
class ClassName:
    # Class constructor to initialize attributes
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1  # Assigning attributes to the object
        self.attribute2 = attribute2
    
    # Method to perform some action
    def method1(self):
        # Accessing attributes and performing actions
        print(f"Attribute 1 is {self.attribute1}")
```
### ***Syntax for creating an object*** 
```python
# Creating an object of the class
object_name = ClassName(value1, value2)

# Accessing attributes and methods
print(object_name.attribute1)  # Access an attribute
object_name.method1()  # Call a method
```
### Example 

```python 
# Define the Car class
class Car:
    # Constructor to initialize the car's attributes
    def __init__(self, make, model, year):
        self.make = make     # Attribute for the car's make
        self.model = model   # Attribute for the car's model
        self.year = year     # Attribute for the car's year

    # Method to display the car's details
    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

    # Method to simulate starting the car
    def start_engine(self):
        print(f"{self.make} {self.model}'s engine has started.")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Accessing the object's attributes and methods
car1.display_details()  # Output: Car Details: 2020 Toyota Corolla
car2.start_engine()     # Output: Honda Civic's engine has started.
```
## **Logic Breakdown**

1. Class Definition (Car):

* A class named Car is defined, which serves as a blueprint for creating car objects.

* The __init__(self, make, model, year) method is a constructor that initializes the attributes (make, model, and year) of each car object when it is created.

2. Attributes:

* self.make: Stores the car's manufacturer (e.g., Toyota, Honda).

* self.model: Stores the car's model (e.g., Corolla, Civic).

* self.year: Stores the car's year of manufacture (e.g., 2020, 2022).

3. Methods:

* display_details(self): This method prints the car's details (year, make, and model) in a formatted string.

* start_engine(self): This method prints a message indicating that the car’s engine has started, showing the make and model.

4. Creating Objects:

* car1 = Car("Toyota", "Corolla", 2020): Creates an instance of the Car class with the attributes for a Toyota Corolla from 2020.

* car2 = Car("Honda", "Civic", 2022): Creates another instance for a Honda Civic from 2022.

5. Calling Methods:

* car1.display_details(): Calls the display_details method on car1 and prints its attributes.

* car2.start_engine(): Calls the start_engine method on car2 to simulate starting its engine.
  
# **6. Prime Numbers and Fibonacci Series using Class**

```python
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
```

This program defines a class PrimeandFib that includes methods to generate Fibonacci numbers and find prime numbers within a specified range. It takes user input to generate both the Fibonacci series and a list of prime numbers and displays the results.

# **Logical Breakdown**

1. Class Definition:

The class PrimeandFib contains three methods:

A. prime(self, num): A helper method to check whether a number is prime.

B. prime_in_range(self, start, end): Generates a list of prime numbers within a given range.

C. fibonacci(self, number): Generates the Fibonacci series for a given number of terms.

2. Method Descriptions:

A. Prime Check (prime(self, num)):

a. Purpose: This method checks if a number is a prime number.

b. Logic:

* If the number is less than 2, it returns False because primes are greater than 1.

* It iterates from 2 up to num-1 and checks if the number is divisible by any of these values.

* If it finds any divisors, it returns False, meaning the number is not prime.

* If no divisors are found, it returns True, meaning the number is prime.

B. Finding Prime Numbers (prime_in_range(self, start, end)):

a. Purpose: This method generates all prime numbers within a specified range.

b. Logic:

* It initializes an empty list primes to store the prime numbers.

* It iterates through the range of numbers from start to end (inclusive).

* For each number in the range, it calls the prime() method to check if the number is prime.

* If the number is prime, it is added to the primes list.

* Finally, it returns the list of all prime numbers found in the range.

C. Fibonacci Sequence (fibonacci(self, number)):

a. Purpose: This method generates the Fibonacci series up to the given number of terms.

b. Logic:

* It initializes two variables a and b to 0 and 1, representing the first two terms of the Fibonacci sequence.

* It creates an empty list fibo_sequence to store the sequence.

* It then iterates number times, appending the value of a (the current Fibonacci number) to the list.

* After appending, it updates a and b so that a takes the value of b, and b takes the value of a + b, generating the next term in the series.

* The method returns the list of Fibonacci numbers
.
3. Input Section:

A. User Input:

* The user is prompted to enter a number to generate the Fibonacci sequence (number).

* The user is also prompted to enter a range (start and end) to find prime numbers within that range.

4. Object Creation:

* An object prime_and_fib_obj of class PrimeandFib is created.

* The object is used to call the methods for generating the Fibonacci sequence and prime numbers.

5. Generating the Results:
   
* fibo_series = prime_and_fib_obj.fibonacci(number):
The Fibonacci sequence is generated using the input number, and the result is stored in the list fibo_series.

* prime_numbers = prime_and_fib_obj.prime_in_range(start, end):

* The prime numbers within the specified range are generated and stored in the list prime_numbers.

6. Displaying the Results:
   
Fibonacci Series: 

* The list of Fibonacci numbers is printed using ', '.join(map(str, fibo_series)) to join the numbers into a comma-separated string.

Prime Numbers:
  
* Similarly, the list of prime numbers is printed in the same format.


### ***Output***
```python
Enter the number for Fibonacci series: 6
Enter the start of the range: 10
Enter the end of the range: 20
Fibonacci Series: 0, 1, 1, 2, 3, 5
Prime Numbers: 11, 13, 17, 19
```

# **7. getattr() in Python**

The getattr() function in Python is a built-in function that allows you to retrieve an attribute from an object dynamically. It is particularly useful when you want to access an attribute whose name is not known until runtime. This function provides a way to handle attributes safely by allowing you to specify a default value to return if the attribute does not exist.

## ***Syntax***

```python
getattr(object, name[, default])
```
* object: The object from which you want to retrieve the attribute.

* name: A string that represents the name of the attribute you want to access.

* default (optional): A value to return if the specified attribute does not exist. If this argument is not provided and the attribute is not found, an AttributeError is raised.

Returns

* The value of the specified attribute if it exists.

* The default value if the attribute does not exist and the default argument is provided.

* Raises an AttributeError if the attribute does not exist and no default is provided.
  
## **Example**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create an instance of Book
book = Book("1984", "George Orwell")

# Accessing attributes using getattr
print("Title:", getattr(book, 'title'))       # Output: Title: 1984
print("Author:", getattr(book, 'author'))     # Output: Author: George Orwell

# Attempting to access a non-existent attribute
print("Publisher:", getattr(book, 'publisher', 'Unknown Publisher'))  # Output: Publisher: Unknown Publisher
```
### **Explanation**

1. Class Definition:

* The Book class is defined with an __init__ method that initializes two attributes: title and author.

2. Object Creation: 

* An instance of the Book class named book is created with the title "1984" and the author "George Orwell".

3. Using getattr(): 

* The code uses the getattr() function to access the title and author attributes of the book object, allowing for dynamic attribute retrieval.

4. Default Value for Non-existent Attribute: 

* When attempting to access the publisher attribute (which does not exist), it uses a default value of "Unknown Publisher" to prevent an error.
  
### ***Output***
```python
Title: 1984
Author: George Orwell
Publisher: Unknown Publisher
```

# **8. Prime Number using getattr()**

```python
class Primenumber:
    def prime(self,num):
        if num<2:
            return False
        for i in range(2,num):
            if num%i==0:
                return False
        return True

    def prime_in_range(self,start, end): 
        for num in range(start, end + 1): #iterate through start and end
            if getattr(self,'prime')(num):
                print(num,end=" ")

# Input
start = int(input("Enter the start of the range:"))
end = int(input("Enter the end of the range: "))

prime_obj=Primenumber()

# Finding and printing prime numbers in the range
print(f"Prime numbers between {start} and {end} are:")
prime_obj.prime_in_range(start, end)
```

# **Logical Breakdown**

1. Class Definition: 

* The Primenumber class is defined to contain methods related to prime number calculations.

2. prime Method:

* This method checks if a given number (num) is prime.
  
* It returns False if the number is less than 2 or if it finds any divisors (i.e., if num is divisible by any integer from 2 to num - 1).

* It returns True if the number is prime.

3. prime_in_range Method:

* This method takes a start and an end value to find all prime numbers in that range.

* It iterates through each number in the specified range and uses getattr(self, 'prime') to dynamically call the prime method.

* If a number is prime, it prints that number.

4. User Input:

* The program prompts the user to enter a start and end value for the range.

5. Finding and Printing Prime Numbers:

* An instance of the Primenumber class is created.
The prime_in_range method is called on this instance to find and print all prime numbers within the specified range.

# **9.Best Time To Buy and Sell Stock**

The task is to calculate the maximum profit that can be achieved from a series of stock prices.

**Code**
```python
class Buyandsell:
    def maxProfit(self,prices):
            total_profit =0
            for i in range(0,len(prices)-1):
                if prices[i+1]>prices[i]:
                    total_profit += prices[i+1]-prices[i]
            return total_profit
prices=[7,1,5,3,6,4]
maxp=Buyandsell()
print("Total profit is:",maxp.maxProfit(prices))
```
## **Explanation**

1. Class Definition: 

* The Buyandsell class is defined to encapsulate the logic for calculating the maximum profit from stock prices.

2. maxProfit Method:

* This method takes an array of stock prices as input (prices).

* It initializes a variable total_profit to store the cumulative profit.

* The method iterates through the prices array, comparing each day's price with the next day's price:

* If the price on the next day (prices[i + 1]) is greater than the price on the current day (prices[i]), it indicates a potential profit.

* The profit from this transaction (prices[i + 1] - prices[i]) is added to total_profit.
  
3. Calculation:

* The method returns the total profit after checking all possible transactions.

4. Execution:

* An instance of the Buyandsell class is created.
The maxProfit method is called with the sample prices array [7, 1, 5, 3, 6, 4], and the result is printed.


### ***Output***

```python
Total profit is: 7
```



