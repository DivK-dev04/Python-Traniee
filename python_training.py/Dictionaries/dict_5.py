# 5. Merge Two Dictionaries
# Create another dictionary called extra_info:

# 'hobbies': 'Reading'
# 'pet': 'Dog'
# Task: Merge extra_info into the person dictionary and print the final merged dictionary.

person = {'name': 'RDJ', 'age': 31, 'city': 'New York', 'occupation': 'Engineer', 'height': '190cm'}
extra_info = {'hobbies': 'Reading','pet': 'Dog'}

person.update(extra_info)                                        #update is use to merge two dict also
print(f"Updated dict : {person}")