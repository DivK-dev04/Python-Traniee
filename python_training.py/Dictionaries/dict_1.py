# 1. Create and Access a Dictionary
# Create a dictionary called person with the following key-value pairs:
# 'name': 'Alice'
# 'age': 30
# 'city': 'New York'
# Task: Access the value of 'city' from the person dictionary and print it

person = {'name': 'Alice', 'age': '30' ,'city': 'New York'}
print(person)
print("THIS IS LIST FROM DICT")
for key, value in person.items():
    print(f"{key} : {value}")

# print("YYYY")
print(person.get("name"))                                        #with get() method

print(person["age"])                                             #with traditional method 
print(person["city"])