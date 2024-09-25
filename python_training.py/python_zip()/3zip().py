names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

z = zip(names, scores)

for name ,score in z:                                    #can also be written as -->  for name, score in zip(names, scores)
    print(f"{name} : {score}")