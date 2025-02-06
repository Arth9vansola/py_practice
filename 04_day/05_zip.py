# # 1. zip() – Combining Multiple Iterables
# # The zip() function combines multiple iterables (e.g., lists, tuples) element-wise into tuples.
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]

# # Using zip()
# combined = list(zip(names, ages))
# print(combined)  
# # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# # unziping

# zipped_data = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
# names, ages = zip(*zipped_data)

# print(names)  # Output: ('Alice', 'Bob', 'Charlie')
# print(ages)   # Output: (25, 30, 35)
