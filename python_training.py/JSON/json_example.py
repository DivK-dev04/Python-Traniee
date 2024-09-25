import json                                                                                   #import json module

with open('/home/nhz/Desktop/New Folder/python_training.py/JSON.py/example.json') as file:    #json FILE as input
    data = json.load(file)                                                                    #load JSON file to convert into python 

print(data)                                                                                   #print the python , converted data

print(data['employees'][1]['name'])

print(data['company']['name'])