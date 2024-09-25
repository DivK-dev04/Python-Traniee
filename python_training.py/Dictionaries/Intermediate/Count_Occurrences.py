# Count Occurrences in a List
# Given the list colors = ['red', 'blue', 'red', 'green', 'blue', 'blue'], count how many times each color appears in the list and store the result in a dictionary.
# Task: Print the dictionary showing color counts.

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
count = {}

for c in colors:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

print(count)