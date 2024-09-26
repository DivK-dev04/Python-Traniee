# Remove Keys with a Specific Condition
# Given the dictionary inventory = {'apples': 10, 'bananas': 0, 'oranges': 5, 'pears': 0}, remove all key-value pairs where the value is 0.
# Task: Print the updated dictionary.

inventory = {'apples': 10, 'bananas': 0, 'oranges': 5, 'pears': 0}

# for key,value in inventory.items():
#     if value == 0:
#         inventory.pop(key)
# print(inventory)

keys_to_remove = [key for key, value in inventory.items() if value == 0]

for key in keys_to_remove:
    del inventory[key]

print(inventory)
