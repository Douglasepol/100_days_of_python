def merge_and_sort_lists(list1, list2):
    '''
    Merges two lists of integers and returns a single sorted list.

    Returns:
    list: A merged and sorted list of integers.
    '''
    # Merge the two lists
    merged_list = list1 + list2

    # Sort the merged list
    merged_list.sort()

    return merged_list

# Example usage:
list1 = [3, 1, 4]
list2 = [2, 5, 6]
print("Merged and sorted list:", merge_and_sort_lists(list1, list2))
