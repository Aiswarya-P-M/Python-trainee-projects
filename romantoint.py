def romantoint(roman):  #creating function romantoint for converting the given roman into integer value
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  #dictionary that contains the roman letter as a key and corresponding integer value as value
    result = 0  #Initialze result as zero
    for i in range(len(roman)): #looping through the input string
        if roman[i] in roman_dict: #check whether the input string is in the dictionary or not
            result += roman_dict[roman[i]] #if the input string is found,add the integer value of the current roman numeral to the result
        else: #if the input string is not found in the dictionary return false
            return False

    return result # return result
roman="VII"
print(romantoint(roman))