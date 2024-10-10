### **1 Variables** ### 

Python has no command for declaring variables. A variable is instantiated when it is first assigned a value.

```python
Age = 24
print(Age)
```

We can assign same value to multiple variable in a single statement.
```python
x=y=z=4
print(x)
print(y)
print(z)
```
We can assign multiple values to multiple variable in a single statement.

```python
name,age='Anu',24
print(name,age)
```
Python is case-senitive. The variable name age and AGE are different. 

### **2 Datatypes in Python** ###

a. int

b. float

c. string

d. list

e. tuple

f. dictionary

g. set
 
**a. int**  : Numeric data without decimal point.
```python
score=100
```

**b. float**  : Numeric data with decimal point.
```python
score=95.5
```
**c. string**  : String is a sequence of characters enclosed in single quotes or double quotes.It is immutable.
```python
Place="Kochi"
```
**d. list**  : In Python, a list is a built-in data type.Lists are defined by enclosing elements in square brackets ([]), with each element separated by a comma.List is ordered, changeable and allow duplicate values.
```python
thislist =[1,2,3]
```
**e. tuple**  : A tuple is a collection which is ordered and unchangeable and allow duplicate values. In tuple element are enclosed within round brackets.
```python
newtuple =(1,2,3)
```
**f. dictionary**  : A dictionary is a collection which is ordered, changeable and do not allow duplicates.Dictionaries are written with curly brackets, and have keys and values.
```python
newdict ={'name':'Ram','age':24}
```
**f. set**  :  A set is a collection which is unordered, unchangeable and duplicate values are not allowed.Sets are written with curly brackets.
```python
newset={1,2,3}
```

### **3 Operations on datatypes** ###

**A. String**

***a.Slicing***

We can return a range of characters by using the slice syntax. The syntax for slicing is: string[start:stop:step] where, 

start: The starting index (inclusive), where slicing begins.

stop: The ending index (exclusive), where slicing ends.

step: The step (optional), which determines the stride or interval between characters.

***a.1 Slicing with start and stop***

```s = "Python Programming"
    substring = s[0:6]  # Output: 'Python'
```
***a.2 Omitting the start index***

If you omit the start index, the slicing starts from the beginning of the string:

```python 
substring = s[:6]  # Output: 'Python'
```
***a.3 Omitting the stop index***

If you omit the stop index, the slicing continues to the end of the string:

```python
eg: substring = s[7:]  # Output: 'Programming'
```

***a.4 Slicing with step***

The step value controls how many characters to skip. 

```python s = "abcdef"
    substring = s[0:6:2]  # Output: 'ace' (every 2nd character from index 0 to 5)
```

***a.5 Reversing a string using step***

```python 
reversed_string = s[::-1]  # Output: 'gnimmargorP nohtyP'
```
 
***a.6 Slicing with negative indices***

``` python s = "Python"
    substring = s[-6:-3]  # Output: 'Pyt' (from index -6 to -4)
```

***a.7 Combining negative indices with step:***

``` python s = "Python"
    substring = s[-6:-3]  # Output: 'Pyt' (from index -6 to -4)
```
***b. Uppercase***

The upper() method returns the string in upper case:

```python a = "Hello, World!"
    print(a.upper())
```

***c. Lowercase***

The lower() method returns the string in lower case:

```python a = "Hello, World!"
    print(a.lower())
```

***d. Concatenation***

To concatenate, or combine, two strings you can use the + operator.
```python a = "Hello"
    b = "World"
    c = a + b
    print(c) #output HelloWorld
```

***e. Length of string***

To get the length of a string, use the len
() function.

```python a = "Hello, World!"
    print(len(a)) #output 13
```

**B. List**

***a. Adding Elements to a List***

***a.1 append()*** : Adds an element to the end of the list.

```python my_list = [1, 2, 3]
   my_list.append(4)
   print(my_list)  # Output: [1, 2, 3, 4]
```   

***a.2 insert()*** : Inserts an element at a specific index.

```python my_list.insert(1, 'a')
   print(my_list)  # Output: [1, 'a', 2, 3, 4]
```

***a.3 extend()*** : Adds multiple elements (from another list or iterable) to the end of the list.

```python my_list.extend([5, 6])
   print(my_list)  # Output: [1, 'a', 2, 3, 4, 5, 6]
```

***b. Removing Elements from a List***

***b.1 remove()*** : Removes the first occurrence of a specified value.

```python my_list.remove('a')
    print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```

***b.2 pop()*** : Removes and returns the element at a specified index. If no index is specified, it removes the last element.

```python popped_element = my_list.pop(2)
   print(popped_element)  # Output: 3
   print(my_list)  # Output: [1, 2, 4, 5, 6]
```

***b.3 clear()*** : Removes all elements from the list.

```python my_list.clear()
    print(my_list)  # Output: []
```

***c.Modifying Elements in a List***

***c.1 Indexing*** : You can modify an element by directly accessing it using its index.

```python my_list = [1, 2, 3]
   my_list[1] = 'b'
   print(my_list)  # Output: [1, 'b', 3]
```

***c.2 Slicing*** : Modify multiple elements at once using slicing.

```python my_list[1:3] = [20, 30]
   print(my_list)  # Output: [1, 20, 30]
```

***d. Length of list***

len(): Returns the number of elements in the list.

```python length = len(my_list)  # Output: 3
```

***e.reverse of a list***

reverse(): Reverses the elements of the list in place.

```python my_list.reverse()
   print(my_list)  # Output: [5, 4, 3, 2, 1]
```

***f. Join Two Lists***

There are several ways to join, or concatenate, two or more lists in Python.
One of the easiest ways are by using the + operator.

```python list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) #output ['a', 'b', 'c', 1, 2, 3]
```

**C. Tuple**

In Python, a tuple is an immutable, ordered collection of elements, similar to a list. However, unlike lists, tuples cannot be changed once created.

***a. Accessing Elements***

You can access tuple elements by their index, similar to lists:
```python my_tuple = (10, 20, 30, 40)
    print(my_tuple[1])  # Output: 20
```

You can also use negative indexing to access elements from the end:

```python my_tuple = (10, 20, 30, 40)
   print(my_tuple[-1])  # Output: 40
```

***b. Slicing***

You can slice a tuple to get a subset of its elements:

```python my_tuple = (10, 20, 30, 40, 50)
   sub_tuple = my_tuple[1:4]  # Output: (20, 30, 40)
```

Slicing can also use negative indices and step:

```python 
sub_tuple = my_tuple[::-1]  # Reverses the tuple: (50, 40, 30, 20, 10)
```

***c. Concatenation***

You can concatenate two or more tuples using the + operator:

```python tuple1 = (1, 2)
   tuple2 = (3, 4)
   new_tuple = tuple1 + tuple2  # Output: (1, 2, 3, 4)
```

***d. Length of a Tuple***

You can find out how many elements are in a tuple using the len() function:

```python my_tuple = (1, 2, 3)
    print(len(my_tuple))  # Output: 3
```

***e. Adding Items to a Tuple***

Using Concatenatio we can create a new tuple by concatenating the existing tuple with another tuple that contains the new items.

```python
 # Original tuple
    my_tuple = (1, 2, 3)

    # New item to add
    new_item = (4,)

    # Concatenating
    new_tuple = my_tuple + new_item
    print(new_tuple)  # Output: (1, 2, 3, 4)
```

***f. Remove items***

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

```python thistuple = ("apple", "banana", "cherry")
   y = list(thistuple)
   y.remove("apple")
   thistuple = tuple(y)
```

Or you can delete the tuple completely:

The *del* keyword can delete the tuple completely:

```python
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists.
``` 

 ***D. Dictionary*** 

***a. Accessing Items***

You can access the items of a dictionary by referring to its key name, inside square brackets:

```python 
thisdict =	{
       "brand": "Ford",
       "model": "Mustang",
        "year": 1964
   }
  x = thisdict["model"]
  print(x) #output Mustang
```

***b. Get Keys***

The keys() method will return a list of all the keys in the dictionary.

```python 
thisdict = {
       "brand": "Ford",
        "model": "Mustang",
        "year": 1964
      }
    x = thisdict.keys()
   print(x) #output dict_keys(['brand', 'model', 'year'])
```

***c. Get Values***

The values() method will return a list of all the values in the dictionary.

```python 
thisdict = {

       "brand": "Ford",
        "model": "Mustang",
        "year": 1964
      }
    x = thisdict.values()
   print(x) #output dict_values(['Ford', 'Mustang', 1964])
```

***d. Change Values***

We can change the value of a specific item by referring to its key name:

```python 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
```

***e. Update Dictionary***

The update() method will update the dictionary with the items from the given argument. The argument must be a dictionary, or an iterable object with key:value pairs.

```python 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
```

***f. Adding items***

Adding an item to the dictionary is done by using a new index key and assigning a value to it:

```python
 thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict) 
```

we can also add item using update method.

```python 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
```

***g. Remove items***

There are several methods.

***g.1 pop***: The pop() method removes the item with the specified key name:

```python 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
```

***g.2 popitem***: The popitem() method removes the last inserted item.

```python 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
```

***g.3 del*** : The del keyword removes the item with the specified key name:

```python 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
```

***g.4 clear*** : The clear() method empties the dictionary:

```python 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
```

**E. Set**

***a. Add Items***: To add one item to a set use the add() method.

```python
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
```
 
***b. Add Sets***: To add items from another set into the current set, use the update() method.

```python 
thisset = {"apple", "banana", "cherry"}
ts = {"pineapple", "mango", "papaya"}
thisset.update(ts)
print(thisset)
```

***c. Add Any Iterable***: The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

```python 
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
```

***d. Remove Item***: To remove an item in a set, use the remove(), or the discard() method.

```python
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
```

***e. Union***: The union() method returns a new set with all items from both sets.
```python 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
```

***f. Intersection***: The intersection() method will return a new set, that only contains the items that are present in both sets.

```python 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
```

***g.Difference***: The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

```python
   set1 = {"apple", "banana", "cherry"}
   set2 = {"google", "microsoft", "apple"}
   set3 = set1.difference(set2)
   print(set3)
```

***h. Symmetric Differences***: The symmetric_difference() method will keep only the elements that are NOT present in both sets.Keep the items that are not present in both sets:

```python
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set3 = set1.symmetric_difference(set2)
    print(set3)
```

### **4 Conditional Statement in Python** ###

Conditional statements in Python allow you to execute specific blocks of code based on whether a condition is true or false. The primary conditional statements in Python are if, elif, and else. Here’s a breakdown of how to use them:

***a. if Statement***: The if statement checks a condition and executes a block of code if the condition is true.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

***b. elif Statement***: The elif (short for "else if") statement allows you to check multiple expressions for truthiness and execute a block of code for the first true condition.

```python
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
```

***c. else Statement***: The else statement is executed if none of the preceding conditions are true.

```python
x = 2
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

### **5 Loop in Python** ###

***a. for Loop***: The for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or any iterable object.

*syntax*: for variable in iterable:
          # Code to execute

```python          
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
We can use range function to generate a sequence of numbers.

```python
 for i in range(5):  # This will generate numbers from 0 to 4
    print(i)
```

***b. While Loop***: The while loop repeatedly executes a block of code as long as a specified condition is true.

*syntax*: while condition:
        # Code to execute

```python 
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count
```

### **6 Casting in Python** ##

Casting in Python refers to converting a variable from one data type to another. This is useful when you need to ensure that operations between different types of data are performed correctly. Python provides several built-in functions for casting between various types. 

***a. Casting to Integer (int())***: We can convert a float or a string containing a number to an integer.
 
*1. From Float to Integer*

```python
float_value = 3.14
int_value = int(float_value)
print(int_value)  # Output: 3
```

*2. From String to Integer*

```python
string_value = "123"
int_value = int(string_value)
print(int_value)  # Output: 123
```

***b. Casting to Float (float())***

*1. From Integer to Float*

```python
int_value = 5
float_value = float(int_value)
print(float_value)  # Output: 5.0
```

*2. From String to Float*

```python
string_value = "2.718"
float_value = float(string_value)
print(float_value)  # Output: 2.718
```
 
***c. Casting to String (str())***

*1. From Integer to String*

```python
int_value = 42
string_value = str(int_value)
print(string_value)  # Output: "42"
```

*2. From Float to String*

```python
float_value = 3.14159
string_value = str(float_value)
print(string_value)  # Output: "3.14159"
```

***d. Casting to List (list())***

*1. From String to List*

```python
string_value = "hello"
list_value = list(string_value)
print(list_value)  # Output: ['h', 'e', 'l', 'l', 'o']
```

*2. From Tuple to List*

```python
tuple_value = (1, 2, 3)
list_value = list(tuple_value)
print(list_value)  # Output: [1, 2, 3]
```

***e. Casting to Tuple (tuple())***

```python
list_value = [1, 2, 3]
tuple_value = tuple(list_value)
print(tuple_value)  # Output: (1, 2, 3)
```

***f. Casting to Set (set())***

```python
list_value = [1, 2, 2, 3]
set_value = set(list_value)
print(set_value)  # Output: {1, 2, 3}
```








