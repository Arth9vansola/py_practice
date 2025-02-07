# 1. Sorting using heapq (Heap Sort)
# The heapq module provides heap-based functions.
# It implements a min-heap (smallest element at the top).
# Best for getting the smallest or largest k elements efficiently.
# Time Complexity: O(n log k) for heapq.nlargest / heapq.nsmallest.

# import heapq

# nums = [5, 2, 9, 1, 5, 6]

# # Convert list into a min-heap
# heapq.heapify(nums)
# print(nums)  # Min-heap structure (not fully sorted)

# # Get smallest element (heap root)
# print(heapq.heappop(nums))  # 1 (smallest element)

# # Get 3 smallest numbers
# print(heapq.nsmallest(3, nums))  # [2, 5, 5]

# # Get 3 largest numbers
# print(heapq.nlargest(3, nums))  # [9, 6, 5]
