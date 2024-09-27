# Remove Keys with Values Below a Threshold
# Given the dictionary scores = {'Alice': 85, 'Bob': 45, 'Charlie': 70, 'David': 90}, remove all key-value pairs where the value is less than 70. Print the updated dictionary.

scores = {'Alice': 85, 'Bob': 45, 'Charlie': 70, 'David': 90}
updated_dict = {}

for key,value in scores.items():
    if value >= 70:
        updated_dict[key] = value
print(updated_dict)
