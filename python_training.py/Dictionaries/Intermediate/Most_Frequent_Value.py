# Find the Most Frequent Value
# Given a dictionary items = {'apple': 4, 'banana': 2, 'orange': 4, 'kiwi': 3}, find the value that occurs most frequently. If there are ties, return all keys with that value in a list.

items = {'apple': 4, 'banana': 2, 'orange': 4, 'kiwi': 3}
count = {}

for value in items.values():
    if value in count:
        count[value] += 1
    else:
        count[value] = 1
max_count = max(count.values())

k = [key for key, value in items.items() if value == max(count, key=count.get)]

print("Most frequent value:", max(count, key=count.get))
print("Keys with that value:", k)