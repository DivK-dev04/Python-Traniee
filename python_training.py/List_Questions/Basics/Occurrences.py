#Write a function to count how many times each element appears in list1 and list2.

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4]

l= list1 + list2
occur = {}

for x in l:
    if x in occur:
        occur[x] += 1               # If element x is already in the dictionary, increase its count by 1
    else :
        occur[x] = 1                # If element x is not in the dictionary, add it and set its count to 1

print(occur)