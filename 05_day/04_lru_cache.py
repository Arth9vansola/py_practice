# Dynamic Programming with Memoization (@lru_cache)
# Dynamic Programming (DP) is an optimization technique used to solve problems by breaking them into overlapping subproblems. Memoization is a method to store results of expensive function calls to avoid redundant computations.

# Python provides an easy way to implement memoization using functools.lru_cache.

# 🔹 What is @lru_cache?
# @lru_cache (Least Recently Used Cache) is a built-in decorator that automatically caches function results based on input arguments.

# ✅ Benefits of @lru_cache:
# Avoids recomputation of the same inputs.
# Improves performance for recursive solutions.
# Simple to implement (just one line of code).
# Works only with hashable arguments (e.g., numbers, strings, tuples, but not lists, dictionaries and set).
# it is  immutable

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)

# print(fib(35))  # Takes a long time due to repeated calculations!

# from functools import lru_cache

# @lru_cache(None)  # No limit on cache size
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
# print(fib(3))  # Much faster due to memoization!
# fib.cache_clear()  # Clears stored results for fresh calculations

# Example with Limited Cache Size
# @lru_cache(maxsize=5)  # Store only last 5 results
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(10))  # Computes factorial(10) and caches results



