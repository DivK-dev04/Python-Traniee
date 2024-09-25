def person(a):
    return a['age'] > 18                  #fir dict type of data
    
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 15}, {'name': 'Charlie', 'age': 30}, {'name': 'David', 'age': 17}]

x = list(filter(person, people))

print(x)