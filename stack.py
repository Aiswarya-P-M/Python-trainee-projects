def valid_adjusent(input_str: str) -> bool:
    adj_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    stack = []

    for char in input_str: #Iterate through every character in the input string
        if char in adj_pairs.values():
            stack.append(char)  # Push opening brackets onto the stack
        elif char in adj_pairs: # If the character is a closing bracket, check if the stack is not empty and the last item in the stack is the corresponding opening bracket
            if not stack or stack[-1] != adj_pairs[char]:
                return False  # Mismatch brackets
            stack.pop()  # Pop matching opening bracket

    return not stack  # Return True if the stack is empty

print(valid_adjusent('()[]{}'))         
 