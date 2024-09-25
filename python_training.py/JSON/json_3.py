import json

json_data_3 = '{ "make": "Tesla", "model": "Model S", "year": 2020, "electric": true }'

# p2 = json_data_3["make"]                                #showing error bcoz it is not converted into python file to be get accessed 
# print(p2)                                               #becoz it is string and python cannot access string

p = json.loads(json_data_3)

p1 = p["make"]                                            #after convert it we can access it but in above code before conversion it was not doing

print(f"This is JSON data : {json_data_3}")
print(f"This is python data : {p}")
print(p1)