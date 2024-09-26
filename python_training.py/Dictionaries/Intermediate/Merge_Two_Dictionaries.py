# Merge Two Dictionaries
# Given two dictionaries, dict1 = {'a': 1, 'b': 2} and dict2 = {'b': 3, 'c': 4}, merge them into one dictionary. If a key exists in both dictionaries, the value from dict2 should be used.

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)
print(dict1)