
'''



'''


def count_vowels(s):

    vowels = "aeiouAEIOU"
    count = 0

    # Iterate through each character in the string
    for char in s:
        # If the character is a vowel, increment the count
        if char in vowels:
            count += 1

    return count

# Test examples
test_strings = ["Hello World", "Python Programming", "XYZ"]

# Initialize an empty dictionary to store the results
vowel_counts = {}

# Iterate through each string and count its vowels
for string in test_strings:
    vowel_counts[string] = count_vowels(string)

print(vowel_counts)