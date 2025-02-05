# def is_palindrome(s):
#     if len(s) <= 1:  
#         return True  # Base case: Single character or empty string is a palindrome

#     if s[0] != s[-1]:  
#         return False  # If first and last character don't match, it's not a palindrome

#     return is_palindrome(s[1:-1])  # Recursive call with the inner substring

# # Example tests
# print(is_palindrome("madam"))     # Output: True
# print(is_palindrome("racecar"))   # Output: True
# print(is_palindrome("hello"))     # Output: False
# print(is_palindrome("a"))         # Output: True
# print(is_palindrome(""))          # Output: True

#  Dry Run Example: "racecar"
# is_palindrome("racecar")
#     → "r" == "r" ✅ → Call is_palindrome("aceca")

# is_palindrome("aceca")
#     → "a" == "a" ✅ → Call is_palindrome("cec")

# is_palindrome("cec")
#     → "c" == "c" ✅ → Call is_palindrome("e")

# is_palindrome("e")
#     → Base case reached (✅ True)

# Final result: True
