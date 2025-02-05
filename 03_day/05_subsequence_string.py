# from functools import lru_cache

# @lru_cache(None)
# def find_subsequences(s):
#     if not s:
#         return ("",)  # Base case: Only one subsequence (empty string)

#     first = s[0]
#     rest_subsequences = find_subsequences(s[1:])  # Recursive call

#     # Generate subsequences: Exclude first + Include first
#     return rest_subsequences + tuple(first + sub for sub in rest_subsequences)

# # Example usage
# print(find_subsequences("abc"))

# how it works
# find_subsequences("abc")  → first = "a", call find_subsequences("bc")

# find_subsequences("bc")   → first = "b", call find_subsequences("c")

# find_subsequences("c")    → first = "c", call find_subsequences("")

