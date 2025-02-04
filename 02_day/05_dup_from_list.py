numbers = [1, 2, 3, 4, 2, 3, 5, 1]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)  # Output: [1, 2, 3, 4, 5]
