zipped = [('Alice', 85, 24), ('Bob', 90, 25), ('Charlie', 78, 23)]
name , scores , ages = zip(*zipped)

print(name)
print()
print(scores)
print()
print(ages)