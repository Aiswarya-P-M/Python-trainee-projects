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