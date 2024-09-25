import json

json_data_1 = '{ "name": "John", "age": 30, "city": "New York" }'

py_data = json.loads(json_data_1)

print(f"This is JSON data : {json_data_1}")
print(f"This is python data : {py_data}")
