#Write a function to find elements that are in list2 but not in list1

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

l = []

for x in list2:
    if x not in list1:
        l.append(x)

print(l)