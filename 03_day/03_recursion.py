# 1. Factorial Using Recursion
# factorial can be like n! = n * (n-1) * (n-2) * (n-3) * ... * 1

# def factorial(n):
#     if n == 0 or n == 1:  # Base case
#         return 1
#     return n * factorial(n - 1)  # Recursive case

# print(factorial(5))  # Output: 120

# 2. Fibonacci Using Recursion
# it can written as f(n) = f(n-1) + f(n-2)
# base cases are f(0) = 0 and f(1) = 1

# def fibonacci(n):
#     if n == 0:
#         return 0  # Base case
#     elif n == 1:
#         return 1  # Base case
#     return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# print(fibonacci(6))  # Output: 8

# Step-by-Step Execution for fibonacci(6)
# fibonacci(6)
# = fibonacci(5) + fibonacci(4)

#     fibonacci(5)
#     = fibonacci(4) + fibonacci(3)
    
#         fibonacci(4)
#         = fibonacci(3) + fibonacci(2)

#             fibonacci(3)
#             = fibonacci(2) + fibonacci(1)

#                 fibonacci(2)
#                 = fibonacci(1) + fibonacci(0)
#                 = 1 + 0 = 1  ✅

#             fibonacci(3) = 1 + 1 = 2  ✅

#         fibonacci(4) = 2 + 1 = 3  ✅

#     fibonacci(5) = 3 + 2 = 5  ✅

# fibonacci(6) = 5 + 3 = 8  ✅

# 3. Generating All Subsets of a List
# subset means n elements can have 2^n subsets
#  base case is when the list is empty [[]]
# def subsets(arr):
#     if not arr:
#         return [[]]  # Base case: Only one subset (empty set)
    
#     first = arr[0]  # First element
#     rest_subsets = subsets(arr[1:])  # Recursive call on the rest of the list
    
#     return rest_subsets + [ [first] + subset for subset in rest_subsets ]

# print(subsets([1, 2, 3]))



 

