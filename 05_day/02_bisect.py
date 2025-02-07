# Binary Search in Python (bisect module)
# The bisect module in Python provides efficient binary search operations for sorted lists. 
# It allows inserting elements while maintaining order and finding positions efficiently using O(log n) time complexity.

# 🔹 Key Functions in bisect
# Function	                                      Description
# bisect.bisect_left(lst, x)	       Finds the leftmost index to insert x (before existing entries).
# bisect.bisect_right(lst, x)	       Finds the rightmost index to insert x (after existing entries).
# bisect.bisect(lst, x)	               Same as bisect_right().
# bisect.insort_left(lst, x)	       Inserts x at the leftmost valid position while maintaining order.
# bisect.insort_right(lst, x)	       Inserts x at the rightmost valid position while maintaining order.
# bisect.insort(lst, x)	               Same as insort_right().

# 🔹 Finding an Insertion Index
# bisect.bisect_left() and bisect.bisect_right() return the index where x should be inserted in a sorted list.

import bisect

arr = [1, 3, 4, 7, 8, 10]
x = 5

# index = bisect.bisect_left(arr, x)
# print("Insert position (left):", index)  # Output: 3
# 👉 Explanation:

# 5 should be inserted at index 3 (before 7).
# index = bisect.bisect_right(arr, x)
# print("Insert position (right):", index)  # Output: 3

# 👉 Explanation:

# Also returns index 3, but bisect_right() would insert after any existing 5s in the list.

# Inserting While Maintaining Sorted Order
# You can use insort_left() or insort_right() to insert an element directly into the sorted list.
# bisect.insort(arr, x)
# print("Updated List:", arr)  # Output: [1, 3, 4, 5, 7, 8, 10]

# for finding an insertion index of given number
# def binary_search(arr, x):
#     index = bisect.bisect_left(arr, x)
#     # print(index)
#     return index if index < len(arr) and arr[index] == x else -1

# print(binary_search(arr, 7))  # Output: 3 (index of 7)
# print(binary_search(arr, 6))  # Output: -1 (not found)

