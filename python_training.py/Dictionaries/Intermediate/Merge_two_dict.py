# Merge Two Dictionaries
# You have two dictionaries:
# contact_info = {'email': 'john.doe@example.com', 'phone': '555-1234'}
# address = {'city': 'New York', 'zip': '10001'}
# Task: Merge them into one dictionary and print the result.

contact_info = {'email': 'john.doe@example.com', 'phone': '555-1234'}
address = {'city': 'New York', 'zip': '10001'}

contact_info.update(address)
print("Updated dict : contact_info = ",contact_info)