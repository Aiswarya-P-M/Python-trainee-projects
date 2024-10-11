def valid_adjacent(input_str: str) -> bool:
    adj_pair_list = ['()', '[]', '{}', '<>']
    
    #Continue until no pairs can be removed
    while True:
        new_str = input_str  #Start with the current string
        for pair in adj_pair_list:
            new_str = new_str.replace(pair, '')  #Remove all occurrences of valid pairs
        if new_str == input_str:  #If no changes occurred, break the loop
            break
        input_str = new_str  #Update the string for the next iteration
    
    return len(input_str) == 0  #Return True if the string is empty

print(valid_adjacent('{()[]{}>}'))
