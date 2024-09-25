import json

json_data_2 = '{ "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925 }'

a = json.loads(json_data_2)

print(f"This is JSON data : {json_data_2}")
print(f"This is python data : {a}")