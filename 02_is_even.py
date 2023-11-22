
'''

Check if a number is even or odd.

'''

def is_even(number):
    return number % 2 == 0

# Example usage:
num = int(input())
if is_even(num):
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")
