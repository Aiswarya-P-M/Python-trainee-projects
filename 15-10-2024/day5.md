# **Training on 15-10-2024**

# **1. Factorial of a Number**

The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It is denoted by n!

### **Code**
```python
def factorial(number):
    if number<0:
        return False
    elif number==0:
        return 1
    else:
        return number*factorial(number-1)

number=int(input("Enter a number:"))
print(f" The factorial of {number} is:",factorial(number))
```
### **Logic**
1. Base Case for Negative Numbers:

* If the input number is negative, the factorial is not defined, so the function returns False to indicate an invalid input.

2. Base Case for Zero:

* The factorial of 0 is defined as 1. So, if the input number is 0, the function returns 1.

3. Recursive Case:

* For any positive number, the function calls itself recursively. It multiplies the current number by the factorial of the number minus 1, until the base case (when the number reaches 0) is reached. This is the heart of the recursive process.

4. User Input and Output:

* The program takes an integer input from the user and prints the factorial of the number using the factorial function. If the input is valid, it shows the result; otherwise, it returns False for negative inputs.

### ***Output***

```python
Enter a number: 5
The factorial of 5 is: 120
```

# **2. Integer To Roman**

## **Code**
```python
def int_to_roman(input_num: int) -> str:
    # Define the mapping of integers to Roman numerals
    int_dict = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }
    
    # Initialize result string
    roman_str = ''
    
    # iterates through each key-value pair in the dictionary, in descending order
    for value, numeral in int_dict.items():
        # Step 4: Check if the current numeral value can be subtracted from input_num
        while input_num >= value:
            # Step 5: Append numeral to result
            roman_str += numeral
            # Step 6: Subtract value from input number
            input_num -= value
    
    # Step 8: Return the final Roman numeral string
    return roman_str

# Example usage
print(int_to_roman(49))  
```

### ***Output***
```python
Input: 49
Output: 'XLIX'
```

### **Logic of the code**

1. Dictionary of Roman Numerals:

* A dictionary (int_dict) is created to map specific integer values to their corresponding Roman numeral strings. The mapping starts from 1000 and goes down to 1, including special cases like 900 (CM), 400 (CD), 90 (XC), etc.

2. Initialize Roman Numeral String:

* The variable roman_str is used to store the resulting Roman numeral string as we build it.

3. Iterate through the Dictionary:

* The function iterates over each key-value pair in the dictionary (int_dict) in descending order of the values.

4. Build the Roman Numeral:

* For each numeral in the dictionary, the function checks if the input number (input_num) is greater than or equal to the current numeral's value.

* If it is, the corresponding Roman numeral is appended to roman_str, and the value is subtracted from input_num.

* This process repeats until the input number becomes zero.

5. Return the Result:

* Once all numerals are processed and the input number is reduced to zero, the final Roman numeral string is returned.
  
# **3. Reverse Words in a String**

### **Code**
```python
def reverse_words(string):
    words=string.split(" ")
    rev_words=words[::-1]
    reverse_string=" ".join(rev_words)
    return reverse_string

string="the sky is blue"
print("Reverse of word is :",reverse_words(string))
```

### ***Output***
```python
Reverse of word is : the sky is blue
```

### **Logic of the code**

1. Splitting the String:

* The function reverse_words() takes a string as input.
The split(" ") method is used to break the input string into a list of words based on spaces. For example, the string "blue is sky the" becomes ['blue', 'is', 'sky', 'the'].

2. Reversing the List of Words:

* The list of words is reversed using slicing ([::-1]). This creates a new list containing the words in reverse order. For the input list ['blue', 'is', 'sky', 'the'], the reversed list will be ['the', 'sky', 'is', 'blue'].
  
3. Joining the Reversed Words:

* The join(" ") method is then used to concatenate the reversed list of words back into a single string, with each word separated by a space. So ['the', 'sky', 'is', 'blue'] becomes "the sky is blue".
  
4. Returning the Result:

* Finally, the function returns the reversed string.


# **4. Remove Duplicates in a Sorted Array**

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

### **Code**

```python
from collections import Counter

nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]

counts=Counter(nums)
min_count=2
max_count=3
result=[]
for num,count in counts.items():
    if count>=min_count:
        result.extend([num]*min_count)
    elif count==1:
        result.append(num)
    else:
        result=None

underscores_number=len(nums)-len(result)
result.extend(['_']*underscores_number)
print(result)
```
### ***Output***
```python
[0, 0, 1, 1, 2, 3, 3, '_', '_']
```

### **Logic of the code**

1. Import Counter:

* The Counter from the collections module counts occurrences of each element in the list.

2. Count Occurrences:

* The line counts = Counter(nums) generates a dictionary with unique numbers as keys and their counts as values.

3. Initialize Variables:

* Set min_count to 2 and max_count to 3, and initialize an empty list result.

4. Build Result List:

* Iterate through the counts:
If count >= min_count, add the number min_count times to result.

* If count == 1, add the number once.

5. Calculate and Add Underscores:

* Calculate how many underscores are needed: underscores_number = len(nums) - len(result).
  
* Extend result with underscores to match the original list length.

# 5. **Rotate Array**

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

### **Code**
```python
nums=[1,2,3,4,5,6,7]
k=3
arr=[]
length=len(nums)
diff=length-k
arr=nums[diff:]+nums[:diff]
print("The rotated array is:",arr)
```

### ***Code***
```python
The rotated array is: [5, 6, 7, 1, 2, 3, 4]
```
### **Logic of the code**

1. Initial Variables:

* nums = [1, 2, 3, 4, 5, 6, 7]: This is the original array.

* k = 3: This specifies how many steps we want to rotate the array to the right.

2. Calculate Length:

* length = len(nums): This gets the length of the nums array, which is 7 in this case.

3. Calculate the Starting Point for Slicing:

* diff = length - k: This calculates the index where the split will occur. 

* For k = 3, diff becomes 7 - 3 = 4. 

* This means that the last 3 elements will be moved to the front, and the first 4 elements will follow them.

4. Array Slicing:

* arr = nums[diff:] + nums[:diff]: This creates a new array:

* nums[diff:] gives the elements from index 4 to the end of the array: [5, 6, 7].

* nums[:diff] gives the elements from the start of the array up to (but not including) index 4: [1, 2, 3, 4].

* The two slices are concatenated together: [5, 6, 7] + [1, 2, 3, 4].

5. Final Result:

* The resulting array arr is now [5, 6, 7, 1, 2, 3, 4].

6. Output:

* The print statement outputs the rotated array.

