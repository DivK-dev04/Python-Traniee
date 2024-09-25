# 3. Loop Through Dictionary Keys and Values
# Using the updated person dictionary from Question 2, write a loop that prints both the keys and the values in the following format:
# key: value

person = {'name': 'RDJ', 'age': 31, 'city': 'New York', 'occupation': 'Engineer', 'height': '190cm'}
for key,value in person.items():
    print(f"{key} : {value}")