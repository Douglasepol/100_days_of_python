def find_closest_pair(numbers):
    '''
    This function finds a pair of numbers in the list with the smallest absolute difference.
    
    Args:
    numbers (list): A list of integers.

    Returns:
    tuple: A tuple containing the pair of integers with the smallest absolute difference.
    '''
    # Sort the array to ensure that adjacent elements are the closest
    numbers.sort()

    smallest_diff = float('inf')

    closest_pair = (None, None)

    for i in range(len(numbers) - 1):
        # Calculate the difference between the current pair.
        diff = abs(numbers[i] - numbers[i + 1])

        if diff < smallest_diff:
            smallest_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example usage:
numbers = [2, 40, 20, 30, 60, 70]
print("Closest pair:", find_closest_pair(numbers))
