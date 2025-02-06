# def flatten_list(nested_list):
#     """Flattens a nested list into a single list using list comprehension."""
#     return [item for sublist in nested_list for item in sublist]

# # Example usage:
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# flat_list = flatten_list(nested_list)
# print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Another example with mixed data types:
# nested_list_mixed = [[1, 'a', 3], [4.5, True], [6, [7, 8], 9]]  # Note the nested list within
# flat_list_mixed = flatten_list(nested_list_mixed)
# print(flat_list_mixed) # Output: [1, 'a', 3, 4.5, True, 6, [7, 8], 9]


# # Handling arbitrarily nested lists (recursive approach):
# def flatten_deep(nested_list):
#     """Flattens arbitrarily nested lists using recursion."""
#     flat_list = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flat_list.extend(flatten_deep(item)) # Recursively flatten sublists
#         else:
#             flat_list.append(item)
#     return flat_list

# nested_list_deep = [1, [2, [3, 4], 5], 6, [7, 8]]
# flat_list_deep = flatten_deep(nested_list_deep)
# print(flat_list_deep) # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# nested_list_deep_more = [1, [2, [3, [4, 5]]], 6]
# flat_list_deep_more = flatten_deep(nested_list_deep_more)
# print(flat_list_deep_more) # Output: [1, 2, 3, 4, 5, 6]

######################################### explanation ###############################################################

# Let's trace the execution of flatten_deep step by step, using the example nested_list_deep = [1, [2, [3, 4], 5], 6, [7, 8]].

# Initial Call: flat_list_deep = flatten_deep(nested_list_deep)

# flat_list = [] (An empty list is created to store the flattened elements).
# Loop 1: item = 1

# isinstance(1, list) is False.
# flat_list.append(1) flat_list becomes [1].
# Loop 2: item = [2, [3, 4], 5]

# isinstance([2, [3, 4], 5], list) is True.

# flat_list.extend(flatten_deep([2, [3, 4], 5]))  This is a recursive call.  Execution of the current flatten_deep function is paused, and a new call to flatten_deep is made with the sublist [2, [3, 4], 5].

# Recursive Call 1: flatten_deep([2, [3, 4], 5])

# flat_list = [] (A new empty flat_list is created for this recursive call).
# Loop 2.1: item = 2
# isinstance(2, list) is False.
# flat_list.append(2) flat_list becomes [2].
# Loop 2.2: item = [3, 4]
# isinstance([3, 4], list) is True.

# flat_list.extend(flatten_deep([3, 4])) Another recursive call!

# Recursive Call 2: flatten_deep([3, 4])

# flat_list = []
# Loop 2.2.1: item = 3
# flat_list.append(3) flat_list becomes [3].
# Loop 2.2.2: item = 4
# flat_list.append(4) flat_list becomes [3, 4].
# Return: flatten_deep([3, 4]) returns [3, 4].
# The execution returns to Recursive Call 1.

# flat_list.extend([3, 4])  flat_list becomes [2, 3, 4].

# Loop 2.3: item = 5
# isinstance(5, list) is False.
# flat_list.append(5) flat_list becomes [2, 3, 4, 5].
# Return: flatten_deep([2, [3, 4], 5]) returns [2, 3, 4, 5].
# The execution returns to the very first call to flatten_deep.

# flat_list.extend([2, 3, 4, 5])  flat_list becomes [1, 2, 3, 4, 5].

# Loop 3: item = 6

# isinstance(6, list) is False.
# flat_list.append(6) flat_list becomes [1, 2, 3, 4, 5, 6].
# Loop 4: item = [7, 8]

# isinstance([7, 8], list) is True.

# flat_list.extend(flatten_deep([7, 8])) Another recursive call.

# Recursive Call 3: flatten_deep([7, 8])

# flat_list = []
# Loop 4.1: item = 7
# flat_list.append(7) flat_list becomes [7].
# Loop 4.2: item = 8
# flat_list.append(8) flat_list becomes [7, 8].
# Return: flatten_deep([7, 8]) returns [7, 8].
# The execution returns to the very first call to flatten_deep.

# flat_list.extend([7, 8])  flat_list becomes [1, 2, 3, 4, 5, 6, 7, 8].

# Loop finishes.

# Return: The initial call to flatten_deep returns [1, 2, 3, 4, 5, 6, 7, 8].
