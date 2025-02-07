# 🔹 1. deque (Double-Ended Queue)
# A deque (pronounced "deck") is an optimized list-like container that supports fast append and pop operations from both ends (O(1) complexity), 
# compared to a regular list which has O(n) complexity for insertions/removals at the beginning.

# ✅ When to Use deque?
# When you need fast O(1) appends/pops from both ends.
# When implementing stacks and queues efficiently.
# When dealing with sliding window problems.
from collections import deque

# Create a deque
# dq = deque([1, 2, 3])
# print(dq)  # deque([1, 2, 3])

# Append elements (both ends)
# dq.append(4)        # Add to right
# dq.appendleft(0)    # Add to left
# print(dq)  # deque([0, 1, 2, 3, 4])

# Pop elements (both ends)
# dq.pop()        # Remove from right
# dq.popleft()    # Remove from left
# print(dq)  # deque([1, 2, 3])

# Rotate elements
# dq.rotate(1)  # Shift right by 1
# print(dq)  # deque([3, 1, 2])

# dq.rotate(-1)  # Shift left by 1
# print(dq)  # deque([1, 2, 3])

# ✅ deque as a Queue (FIFO)
# queue = deque()
# queue.append("task1")
# queue.append("task2")
# queue.append("task3")

# print(queue.popleft())  # "task1"
# print(queue.popleft())  # "task2"
# print(queue.popleft())

# ✅ deque as a Stack (LIFO)
# queue = deque()
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)

# queue.pop()
# queue.pop()
# queue.pop()
# print(queue)

# 2. Counter (Element Frequency Counting)
# A Counter is a specialized dictionary for counting hashable objects. It’s great for frequency analysis.

# ✅ When to Use Counter?
# Counting elements in a list, string, or iterable.
# Finding the most common elements.
# Quick frequency lookup.

# from collections import Counter

# nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,4]
# count = Counter(nums)
# print(count)  # Counter({4: 5, 3: 3, 2: 2, 1: 1})

# # Get frequency of a specific number
# print(count[3])  # 3 (since 3 appears 3 times)


