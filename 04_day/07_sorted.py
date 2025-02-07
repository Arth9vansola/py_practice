# # The sorted() function sorts elements of an iterable and returns a new sorted list.
# # syntax --> sorted(iterable, key=None, reverse=False)
# # 1.
# numbers = [5, 2, 9, 1, 7]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)  
# # Output: [1, 2, 5, 7, 9]

# # 2.
# numbers = [5, 2, 9, 1, 7]
# sorted_numbers = sorted(numbers,reverse=True)
# print(sorted_numbers)  
# # Output: [1, 2, 5, 7, 9]

# # Example: Sorting with a Custom Key (Sorting by String Length)
# words = ["apple", "banana", "kiwi", "cherry"]
# sorted_words = sorted(words, key=len)
# print(sorted_words)  
# # Output: ['kiwi', 'apple', 'cherry', 'banana']

# nums = [5, 2, 9, 1, 5, 6]
# print(sorted(nums))         # [1, 2, 5, 5, 6, 9]
# print(sorted(nums, reverse=True))  # [9, 6, 5, 5, 2, 1]

# # Sorting a list of tuples by the second value
# data = [(1, 'B'), (3, 'A'), (2, 'C')]
# print(sorted(data, key=lambda x: x[1]))  # [(3, 'A'), (1, 'B'), (2, 'C')]


# The sorted() function returns a new sorted list from an iterable.
# It uses Timsort (a hybrid sorting algorithm based on merge sort and insertion sort).
# It has a time complexity of O(n log n).