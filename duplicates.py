my_list = [1, 1, 1, 1, 2, 2, 2]

# Find the maximum count of any element in the list
max_count = max(my_list.count(num) for num in my_list)

# Find all elements that have the same maximum count
most_frequent = list(set(num for num in my_list if my_list.count(num) == max_count))
#It iterates through each number num in my_list.
#It checks if the count of num is equal to max_count.
#If the condition is true, it yields num.

print(f"The number(s) that appear most often are: {most_frequent}")
