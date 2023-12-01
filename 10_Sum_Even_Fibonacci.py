'''

Problem: Sum of Even Fibonacci Numbers

Write a Python function to calculate the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.

'''

def sum_even_fibonacci(limit):
    a, b = 0, 1
    even_sum = 0
    fibo_sequence = []
    
    # Generate Fibonacci sequence and sum even-valued terms
    while a <= limit:
        fibo_sequence.append(a)
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b
    
    print(fibo_sequence)
    
    return even_sum

# Calculate the sum of even Fibonacci numbers 
result = sum_even_fibonacci(1000)
print(result)
