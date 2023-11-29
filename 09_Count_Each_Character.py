
'''

Problem: Count the Occurrences of Each Character in a String

Write a Python function that takes a string as input and returns a dictionary where the keys are the characters in the string, 
and the values are the number of times each character appears in the string.

'''

def count_characters(s):
    char_counts = {}

    # Iterate over each character in the string
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

test_strings = ["hello", "character"]

character_counts = {}

# Iterate through each string and count the characters
for string in test_strings:
    character_counts[string] = count_characters(string)

print(character_counts)
