# Dictionary from Two Lists
# You have two lists:
# keys = ['name', 'age', 'city']
# values = ['Alice', 30, 'Paris']

# Task: Convert these lists into a dictionary where the items in keys are the dictionary's keys, and the items in values are the values.

keys = ['name', 'age', 'city']
values = ['Alice', 30, 'Paris']

kv = dict(zip(keys,values))                                 #zip used 
print(kv)