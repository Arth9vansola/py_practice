from collections import Counter

def most_frequent(list_):

    if not list_:  # Check for empty list
        return None

    counts = Counter(list_)  # Efficiently counts element occurrences
    return counts.most_common(1)[0][0]  # Returns the most common element


# Example usage:
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
most_common_element = most_frequent(my_list)
print(f"The most frequent element is: {most_common_element}")  # Output: 4

another_list = ['apple', 'banana', 'apple', 'orange', 'apple', 'banana']
most_common_fruit = most_frequent(another_list)
print(f"The most frequent fruit is: {most_common_fruit}") # Output: apple

empty_list = []
most_common_empty = most_frequent(empty_list)
print(f"Most common element in empty list: {most_common_empty}") # Output: None

tie_list = [1, 2, 2, 1, 3] # 1 and 2 are tied
most_common_tie = most_frequent(tie_list)
print(f"Most common element in tie list: {most_common_tie}") # Output: 1 (or 2, order isn't guaranteed)