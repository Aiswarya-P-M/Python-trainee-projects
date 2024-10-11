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
