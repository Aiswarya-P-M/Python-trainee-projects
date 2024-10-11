## 1. Sort a list without using sort function ##

 We can sort a list without using the built-in sort() function by implementing sorting algorithms like Bubble Sort, Selection Sort, Insertion Sort, etc. Here I used bubble sort method for sorting the list. 

 ```python
 list1=[9,2,3,10]
for i in range(len(list1)-1):
    for j in range(len(list1)-1-i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print("sorted list:",list1)
```    
Here we used nested for loop.

## 2. Finding the largest common prefix  ##

```python
def longest_common_prefix(strs):
    '''  
    '''
    if not strs:
        return False

    
    # Start by assuming the first string is the common prefix
    prefix = strs[0]
    
    for s in strs[1:]:
        # Compare the prefix with each string in the list
        while not s.startswith(prefix):
            # Shorten the prefix by one character each time
            prefix = prefix[:-1]
            if not prefix:
                return False
    
    return prefix

# Example usage
strs = ["do", "dog", "door","done"]
print("The longest common prefix is:", longest_common_prefix(strs))
```

We can use another method for finding largest common prefix. For this we can use the sort function.

```python
def longest_common_prefix(strs):
    '''  
    Find the longest common prefix by sorting and comparing the first and last strings.
    '''
    if not strs:
        return ""
    
    # Sort the list and compare only the first and last string
    strs.sort()
    first, last = strs[0], strs[-1]
    
    # Find the longest common prefix between the first and last string
    i = 0 # The variable i is set to 0. It will be used to keep track of the matching characters between the first and last strings.
    while i < len(first) and first[i] == last[i]: #The while loop checks two conditions: (1) i < len(first) ensures we don't go beyond the length of first, and (2) first[i] == last[i] checks if the characters at index i of first and last are the same.
        i += 1 #if both conditions are true then increment i
    
    return first[:i]  # Return the common prefix


# Example usage
strs = ["do", "dog", "door", "done"]
print("The longest common prefix is:", longest_common_prefix(strs))
```

## 3. Converting Roman Numeral to Integer ##

Here I used a dictionary where each Roman numeral is mapped to its integer equivalent for converting the Roman numeral to integer. It loops through each character of the input string, adds its corresponding value to a cumulative `result`, and checks whether each character is valid by confirming its presence in the dictionary. If any character is not a valid Roman numeral, the method returns `False`; otherwise, it returns the total converted value.

```python
def roman_to_integer(input_str:str)->str:
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0 #to keep track of the final value
    previous_val = 0 #Keeps track of the value of the last Roman numeral processed 


    for char in input_str: #The loop processes each character in the input string
        if char in roman_dict: #Check if the character is in the dictionary
            current_val = roman_dict[char] 
            
            if current_val > previous_val: #If the current value  is greater than the previous  value 
                result += current_val - 2 * previous_val #Subtracting 2 * previous_val (to undo the previous addition and subtract the smaller numeral).
            # Adding the current numeral's value (current_val).
            else:
                result += current_val #If the current numeral's value is less than or equal to the previous one, simply add its value to result
            previous_val = current_val #Update previous_val to be the current numeral's value

        else:
            return "Invalid input or out of range"
    return result

print(roman_to_integer('IV'))
```