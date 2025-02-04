# dictionary are mutable
# indexed
# key value pair
# unordered
# key should be unique

d = {
    1: "one", 
    2: "two",
    3: "three",
    "car": "bmw",
}
# print(d.items())
# print(d.keys())
# print(d.values())
# print(d[1])
# print(d.get(2))
# print(d.update({4: "four"}))
# print(d)
# print(d['car'])
d["car"]="rolls royce"
print(d)

#  default value in dictionary
from collections import defaultdict

# Default value for missing keys (default type is `int`, which defaults to 0)
scores = defaultdict(int)

scores["Alice"] += 10
scores["Bob"] += 5

print(scores)  # {'Alice': 10, 'Bob': 5}
print(scores["Charlie"])  # 0 (No KeyError!)

# counter for counting

from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)

print(word_count)  # {'apple': 3, 'banana': 2, 'orange': 1}

# Getting the most common elements
print(word_count.most_common(2))  # [('apple', 3), ('banana', 2)]

# Updating the counter
word_count.update(["apple", "banana", "grape"])
print(word_count)  # {'apple': 4, 'banana': 3, 'orange': 1, 'grape': 1}

# Convert Counter to a dictionary
print(dict(word_count))  # {'apple': 4, 'banana': 3, 'orange': 1, 'grape': 1}


