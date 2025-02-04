dict1 ={
    'naam': 'John',
    'atak': 'Doe',
    'umar': 25
}

dict2 = {
    'name': 'avi',
    'surname': 'nav',
    'age': 22
}

# way 1
# dict3 = {**dict1, **dict2}
# print(dict3)

# way 2
# murged_dict = dict1 | dict2
# print(murged_dict)

# way 3
# dict1.update(dict2)
# print(dict1)

# way 4
dict1 |= dict2
print(dict1)