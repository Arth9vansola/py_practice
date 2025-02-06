# def infinite_numbers():
#     num = 1
#     while True:
#         yield num
#         num += 1

# # Using the generator
# numbers = infinite_numbers()
# print(next(numbers))  # Output: 1
# print(next(numbers))  # Output: 2
# print(next(numbers))  # Output: 3
def infinite_sequence():
    """Generates an infinite sequence of numbers (starting from 0)."""
    num = 0
    while True:
        yield num
        num += 1


# Example usage:
if __name__ == "__main__":
    my_sequence = infinite_sequence()

    # Print the first 10 numbers:
    for _ in range(10):
        print(next(my_sequence))

    # Or, to demonstrate it's truly infinite (within memory limits!):
    # You can keep calling next() as long as you need numbers.
    print(next(my_sequence))  # 10
    print(next(my_sequence))  # 11
    # ... and so on.

    #  Important:  If you try to convert this to a list directly like this:
    #  my_list = list(infinite_sequence())  # This will cause an infinite loop and likely crash your program.
    #  Because list() tries to exhaust the entire generator.  Don't do this!

    # Instead, process the sequence one item at a time (or a small chunk at a time) as needed.
    # Example of processing in chunks (using itertools):
    import itertools

    for chunk in iter(lambda: list(itertools.islice(my_sequence, 5)), []): # Get chunks of 5
        print(f"Processing chunk: {chunk}")
        # Do something with each chunk, e.g., calculations, database inserts, etc.
        for item in chunk:
            # Example: print the square of each number in the chunk
            print(f"Square of {item} is {item*item}")
