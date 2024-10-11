# **Training on 11-10-2024** #

## **1. Decorators** ##

A decorator in Python is a design pattern that allows you to add new functionality to an existing function or method dynamically, without modifying its structure. Decorators are commonly used for cross-cutting concerns like logging, timing, caching, and access control.

### **Syntax** ###

The syntax of a decorator involves two main parts:

1. The decorator function, which takes a function as an argument, enhances it, and returns a modified version.

2. The application of the decorator using the @ symbol before the target function.

```python  
def decorator_function(original_function):
    def wrapper():
        # Add functionality before calling the original function
        print("Something before the function")
        original_function()
        # Add functionality after calling the original function
        print("Something after the function")
    return wrapper
```

### Example ###

```python
# Define a simple decorator
def my_decorator(func):
    def wrapper():
        print("Before the function is called")
        func()
        print("After the function is called")
    return wrapper

# Apply the decorator using @
@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
```

## ***Output*** ##

```python
Before the function
Hello, World!
After the function
```

### Explanation ###

The decorator `my_decorator` is designed to wrap additional functionality around the `say_hello` function. When `say_hello` is called, instead of executing the original function directly, it executes the `wrapper` function defined inside the decorator. The `wrapper` adds behavior before and after calling the original function.

In this case, it prints a message **before** calling `say_hello`, then executes the `say_hello` function itself, and finally prints another message **after** the function is done. This allows you to modify or enhance the behavior of `say_hello` without changing its actual code.


## **2. get() method in Dictionaries** ##

The get() method in Python dictionaries is used to retrieve the value associated with a specified key. It provides a safer way to access dictionary elements compared to using square brackets, as it allows you to handle cases where the key might not exist without raising an error. If the specified key is not found, get() returns None or a specified default value, which makes it particularly useful for avoiding KeyError exceptions.

### *Syntax* ###

```python
dict.get(key, default=None)
```
### *Parameters* ###

* key: The key you want to look up in the dictionary.

* default (optional): The value to return if the specified key does not exist in the dictionary. If not provided, it defaults to None.
  
### Example ###

```python
# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Using get() to access an existing key
name = person.get("name")  # Returns "Alice"

# Using get() to access a non-existing key
country = person.get("country")  # Returns None

# Using get() with a default value
country_with_default = person.get("country", "USA")  # Returns "USA"

# Printing the results
print(name)                   # Output: Alice
print(country)                # Output: None
print(country_with_default)    # Output: USA
```

### Explanation ###

1. Creating a Dictionary: 

* We define a dictionary called person with keys name, age, and city.

2. Accessing an Existing Key:

*  The get() method is used to access the value associated with the key "name". Since "name" exists in the dictionary, it returns "Alice".
  
3. Accessing a Non-Existing Key:

* When we try to access the key "country" using get(), it returns None since that key does not exist in the dictionary. This prevents a KeyError from being raised.
  
4. Using a Default Value:

* We use get() again to access "country" but this time we provide a default value of "USA". Since "country" does not exist in the dictionary, get() returns the default value "USA" instead of None.
  
5. Printing Results: Finally, we print the results of the get() method calls to see the output.

## **3. List Comprehension** 

List comprehension is a concise and efficient way to create lists in Python. It provides a more readable and expressive syntax for generating lists compared to using traditional loops. List comprehensions allow you to create a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string), optionally filtering items based on a condition.

### Syntax ###

```python
new_list = [expression for item in iterable if condition]
```

* expression: The value or operation to be applied to each item.

* item: The variable representing each element in the iterable.

* iterable: Any Python iterable (like a list, tuple, or string).

* condition (optional): A filter that determines whether the item should be included in the new list.
  
### Example 1 ###

Here’s a basic example of using list comprehension to create a list of squares of numbers:

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# List comprehension to create a list of squares
squares = [x ** 2 for x in numbers]

print(squares)  # Output: [1, 4, 9, 16, 25]
```

### *Explanation* ###

* Input List: The original list numbers contains integers from 1 to 5.

* List Comprehension: The expression x ** 2 computes the square of each number in the numbers list.

* Output List: The resulting list squares contains the squares of the original numbers.


### Example 2 ###

We can also add a condition to filter the items included in the new list. Here’s an example that creates a list of even numbers:

```python
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to create a list of even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

### *Explanation* ###

1. Condition: The condition if x % 2 == 0 filters out only the even numbers from the numbers list.

2. Output List: The resulting list even_numbers contains only the even numbers from the original list.

## **Exercises** ##

### 1. Majority Element ###

It counts how many times each element appears and then finds all elements that have the highest frequency. This is particularly useful for understanding the distribution of elements in the list.

## Code ##
```python
my_list = [1, 1, 1, 1, 2, 2, 2]

# Find the maximum count of any element in the list
max_count = max(my_list.count(num) for num in my_list)

# Find all elements that have the same maximum count
most_frequent = list(set(num for num in my_list if my_list.count(num) == max_count))
#It iterates through each number num in my_list.
#It checks if the count of num is equal to max_count.
#If the condition is true, it yields num.

print(f"The number(s) that appear most often are: {most_frequent}")
```

### *Output* ###

```python
The number(s) that appear most often are: [1]
```

The logic of the code is as follows:

1. Count Maximum Frequency: It calculates the maximum occurrence of any element in the list by counting how many times each element appears and determining the highest count.

2. Identify Most Frequent Elements: It then iterates through the list to find all elements that have this maximum count. This is done by checking if the count of each element equals the previously determined maximum count.

3. Store Unique Elements: It uses a set to ensure that only unique elements are stored, removing any duplicates.

4. Output the Result: Finally, it converts the set of most frequent elements back into a list and prints the result, showing the number(s) that appear most often in the original list.

### 2. Palindrome ###

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization. In simpler terms, a palindrome remains unchanged when its characters are reversed. Here we are only consider the alphanumeric characters in the given string.

## Code ##

```python
string1 = input("Enter the string: ")

# Create an empty string called string2 to store only the alphanumeric characters from the original input
string2 = ''

# Iterate through each character in the input string
for char in string1:
    # Check if the character is alphanumeric
    if char.isalnum():
        # Convert to lowercase and add to the string2
        string2 += char.lower()

# Check if the string2 is a palindrome
if string2 == string2[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
```
The logic of the code is as follows:

The provided code snippet checks if a given input string is a palindrome. A palindrome is a sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and case differences. This code filters out only alphanumeric characters from the input, converts them to lowercase, and then checks if the resulting string is a palindrome.

### 3. Best Time To Buy and  Sell ###

Given a list of stock prices where each index represents a day, the code calculates the maximum profit that can be achieved by buying on one day and selling on a future day. It also identifies the specific days for buying and selling based on this maximum profit.

## Code ##

```python
# Given list of prices
a = [7, 1, 3, 4]

max_diff = 0 #max_diff is initialized to 0 to track the maximum price difference found.
buy_day = -1  # Initialize to -1 to indicate no valid day found
sell_day = -1  # Initialize to -1 to indicate no valid day found

# Iterate through the list to find max difference
for i in range(len(a)): #The outer loop iterates through each price in the list using index i.
    for j in range(i + 1, len(a)): #The inner loop iterates through the prices that come after the current price (using index j), specifically starting from i + 1. 
        #This ensures that we only look at future prices to simulate buying first and then selling later.
        diff = a[j] - a[i] #For each pair of prices a[i] (buy price) and a[j] (sell price), the code calculates the price difference:
        if diff > max_diff: #If the calculated difference (diff) is greater than the current max_diff
            #max_diff to the new maximum difference.
            # buy_day to the current index i (the index of the buying day).
            #sell_day to the current index j (the index of the selling day).
            max_diff = diff
            buy_day = i  # Index of buy day
            sell_day = j  # Index of sell day

# Print the best day to buy and sell
if buy_day != -1 and sell_day != -1:
    print(f"Best day to buy: Day {buy_day + 1} (Price: {a[buy_day]})")
    print(f"Best day to sell: Day {sell_day + 1} (Price: {a[sell_day]})")
else:
    print("No profitable buy/sell days found.")
```

The basic logic of the code can be summarized as follows:

1. Initialize Variables: Start by setting up variables to track the maximum profit (max_diff), the best day to buy (buy_day), and the best day to sell (sell_day).

2. Nested Loop: Use two loops:

* The outer loop iterates through each price in the list, treating the current price as the buying price.

* The inner loop iterates through the subsequent   prices, treating each one as a potential selling price.
  
3. Calculate Profit: For each pair of buying and selling prices.

* Calculate the profit as the difference between the selling price and the buying price.

4. Update Maximum Profit: If the calculated profit is greater than the previously recorded maximum profit:

* Update the maximum profit.
* Record the current indices as the best buying and selling days.
  
5. Output Results: After checking all possible pairs:

* If valid buy and sell days are found, print them along with their prices.

* If no profitable transaction is found, print a message indicating that.



