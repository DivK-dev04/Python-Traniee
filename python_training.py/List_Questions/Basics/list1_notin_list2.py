#Write a function to find elements that are in list1 but not in list2.

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

l1 =[]

for x in list1:
    if x not in list2:
        l1.append(x)

print(l1)