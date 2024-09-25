# Remove a Key
# Remove the key 'graduation_year' from the student dictionary.
# Task: Print the dictionary after removing the key.

student =  {'name': 'John', 'age': 21, 'major': 'Computer Science', 'graduation_year': '2025'}
student.pop('graduation_year')                                          #to remove one specific key --> pop
print(student)
# student.popitem()                                                     #to remove last item from the dict  ------------>popitem()
# print(student)