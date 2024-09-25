# 4. Check for a Key
# Using the person dictionary from the previous questions, check if the key 'salary' exists in the dictionary.

# Task: If the key exists, print its value. If not, print "Key not found"

person = {'name': 'RDJ', 'age': 31, 'city': 'New York', 'occupation': 'Engineer', 'height': '190cm'}

# for key in person:
#     if key == 'salary':
#         print(person.get("salary"))                          #it was checking every key and then printing else 5 times 
#     else:
#         print("key not found")



################################corrected version 


if 'salary' in person:                                         #checking all at once then giving only 1 output
    print(person.get('salary'))
else:
    print("key not found")