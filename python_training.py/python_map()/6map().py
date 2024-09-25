words = ['hello', 'world', 'python', 'map']
# Expected Output: [5, 5, 6, 3]


x = list(map(str.__len, words))             #can be done this way also -> x = list(map(len, words))
print(x)