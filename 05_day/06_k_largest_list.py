# import heapq

# def kth_largest(nums, k):
#     return heapq.nlargest(k, nums)[-1]  # Get the Kth largest element

# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 3
# print(kth_largest(nums, k))  # Output: 5
#  another way

import heapq

def kth_largest(nums, k):
    heapq.heapify(nums)  # Convert list into a min-heap
    return heapq.nlargest(k, nums)[-1]  # Extract Kth largest

nums = [7, 10, 4, 3, 20, 15,12]
k = 3
print(kth_largest(nums, k))  # Output: 12
