def binary_search(arr, target, left, right):
    if left > right:
        return -1  # Base case: Target not found

    mid = left + (right - left) // 2  # Calculate mid index

    if arr[mid] == target:
        return mid  # Found the target
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)  # Search left half
    else:
        return binary_search(arr, target, mid + 1, right)  # Search right half

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target, 0, len(arr) - 1)
print(result)  # Output: 3 (index of 7)
