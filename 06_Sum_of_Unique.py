
'''

Problem: Sum of Unique Elements

Write a Python function that takes a list of numbers and returns the sum of all unique elements in the list. 
A number is considered unique if it appears exactly once in the list.


'''

def sum_of_unique(nums):
    # Create a dictionary to count the occurrences of each number
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

    # Sum the numbers that occur exactly once
    unique_sum = 0
    for num in counts:
        if counts[num] == 1:
            unique_sum += num

    return unique_sum

# Example: Calculate the sum of unique elements for a single list
test_list = [4, 4, 5, 6, 7, 8, 8]
unique_sum = sum_of_unique(test_list)
print(unique_sum)