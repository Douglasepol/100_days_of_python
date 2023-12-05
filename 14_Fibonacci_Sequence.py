
'''

	Problem: Fibonacci Sequence Generator
	
	Generate the Fibonacci sequence up to a certain number.
	The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
	
	Returns:
	
	list: A list containing the first n numbers of the Fibonacci sequence.

'''

def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence[:n]

# Test examples
test_numbers = [5, 10, 15, 20]

fibonacci_results = {}

# Iterate through each number and generate its Fibonacci sequence
for number in test_numbers:
    fibonacci_results[number] = fibonacci_sequence(number)

print(fibonacci_results)