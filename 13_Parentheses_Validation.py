def is_valid_parentheses(s):
    """

    Problem: Valid Parentheses String


    Check if a string containing only '(', ')', '{', '}', '[' and ']' is valid.
    A string is valid if:
    1. Open brackets are closed by the same type of brackets.
    2. Open brackets are closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

    Args:
    s (str): The string containing the brackets

    Returns:
    bool: True if the string is valid, False otherwise
    """
    bracket_map = {"(": ")", "{": "}", "[": "]"}
    stack = []

    for char in s:
        if char in bracket_map:
            stack.append(bracket_map[char])
        elif not stack or stack.pop() != char:
            return False

    return not stack

# Test examples
test_strings = ["()", "()[]{}", "(]", "([)]", "{[]}"]

# Initialize an empty dictionary to store the results
validity_results = {}

# Iterate through each string and check if it's valid
for string in test_strings:
    validity_results[string] = is_valid_parentheses(string)

print(validity_results)
