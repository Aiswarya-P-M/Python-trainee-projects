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
print(int_to_roman(49))  # Output: 'MMMDXLIX'
