# 2. Add and Modify a Dictionary
# Starting with the person dictionary from Question 1, add a new key-value pair:

# 'occupation': 'Engineer'
# Then, modify the value of the 'age' key to 31.

# Task: Print the updated dictionary.

person = {'name': 'Alice', 'age': '30' ,'city': 'New York'}
print(person.keys())                                                          #to get to know all keys in dict
print(person.values())                                                        #to get values of keys of dict

person["occupation"] = ("Engineer")                                           #to add new key:value in dict
print(person)

person["age"] = (31)                                                          #to update new value to existing key
print("Updated with age ",person)                                             

person.update({"height" : "190cm"})                                           #to update(and add) with update() 
print(person)

person.update({"name":"RDJ"})
print(person)