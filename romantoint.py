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
        