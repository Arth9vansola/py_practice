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

