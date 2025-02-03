import math  # Import math library for square root function

def is_prime(n):
    # Step 1: Handle base cases
    if n < 2:
        return False  # Numbers < 2 are not prime
    if n in (2, 3):
        return True   # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3
    
    # Step 2: Check factors from 5 to sqrt(n), skipping even numbers
    for i in range(5, int(math.sqrt(n)) + 1, 6):  # Check 6k ± 1 pattern
        if n % i == 0 or n % (i + 2) == 0:
            return False  # If divisible by i or (i + 2), it's not prime
    return True  # If no divisors found, it's prime

# Testing the function
test_numbers = [1, 2, 3, 4, 5, 11, 15, 17, 19, 23, 29, 31, 49, 97, 100]
for num in test_numbers:
    print(f"{num} is Prime: {is_prime(num)}")
