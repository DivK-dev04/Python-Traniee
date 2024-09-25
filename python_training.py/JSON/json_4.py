import json

json_data_4 = '{ "title": "Inception", "director": "Christopher Nolan", "rating": 8.8 }'

q = json.loads(json_data_4)

p = q["director"]
# r = q["title","director","rating"]                               #keyerror coming because , cannot access multiple key value ,have to access seperately
r = q["title"]
s = q["rating"]

print(f"THE TITLE : {r}")
print(f"THE DIRECTOR : {p}")
print(f"THE RATING : {s}")

print(f"This is JSON data : {json_data_4}")
print(f"This is python data : {q}")
