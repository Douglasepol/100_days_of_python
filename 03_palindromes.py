
'''
Problem: Check for Palindromes

Write a Python function that checks if a given string is a palindrome or not. 
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.


For example:

"racecar" is a palindrome.
"hello" is not a palindrome.

Your function should take a string as input and return True if it's a palindrome and False otherwise.
'''

def is_palindrome():
	if word[:] == word[::-1]:
    print(f'{word} is a palindrome.')
else:
    print(f'{word} is not a palindrome.')


word = input()
