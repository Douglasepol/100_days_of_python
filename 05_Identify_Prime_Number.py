
'''

Problem: Identify Prime Numbers

Write a Python function that determines if a given number is a prime number. 
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
For example, 5 is a prime number because it is only divisible by 1 and 5, but 6 is not a prime number because it is divisible by 1, 2, 3, and 6.

The function should:

Take an integer as input.
Return True if the number is prime.
Return False if the number is not prime.

'''

def is_prime(n):
    # Check for edge cases
    if n <= 1:
        return False

    # Check for factors from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# Example: Check if a single number is prime
number_to_check = int(input())
result = is_prime(number_to_check)

print(result)