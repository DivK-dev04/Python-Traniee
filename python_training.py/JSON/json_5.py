import json

json_data_5 = '{ "product": "Laptop", "brand": "Dell", "price": 799.99 }'

z = json.loads(json_data_5)

q = z["product"]
r = z["brand"]
s = z["price"]

print(f"THE LAPTOP DETAILS : {q} , {r} , {s}")
print(f"This is JSON data : {json_data_5}")
print(f"This is python data : {z}")


y = json.dumps(z)
print(f"THIS IS PYTHON TO JSON DATA FROM json.dumps() : {y}")