#  list comprehension
# Using a for loop
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)  # Output: [0, 1, 4, 9, 16]

# --------------------vs----------------------------

# Using list comprehension
squares = [i ** 2 for i in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
