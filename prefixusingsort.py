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
