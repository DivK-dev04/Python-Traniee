#Flatten a List of Dictionaries
#Given a list of dictionaries where each dictionary represents a person with multiple attributes, write a list comprehension to create a list of tuples. Each tuple should contain the person's name and age.

# Tips:

# Extract specific keys from each dictionary.
# Create a tuple with those values.
# Collect these tuples into a new list.

people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]
new_list = []                
for x in people:                                                 #Using tarditional way
    tup = (x["name"],x["age"])
    new_list.append(tup)

print(new_list)

new_list = [(x["name"], x["age"]) for x in people]                #Using List Comprehension
print("LIST COMPREHENSION :: ")
print(new_list) 