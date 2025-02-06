# 2. Generators in Python
# Generators are used to generate values on the fly, rather than storing them in memory. They use lazy evaluation, making them memory-efficient.

# How Generators Work?
# They use the yield keyword instead of return.
# The function remembers its state between calls.
# They are iterators, but they don’t store all values in memory.

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3

