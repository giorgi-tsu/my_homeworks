test_list = [1, 1, 2, 3, 16]


def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the index of the
    target value.

    Parameters:
    - arr (list): A sorted list of elements.
    - target: The value to be searched for.
    
    Returns:
    - int: Index of the target value if found, otherwise None.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid # Target found, return the index
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

target_index = binary_search(test_list, target=1)
print(target_index)