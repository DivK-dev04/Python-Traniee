#Find Common Elements:
#Write a function to find all elements that are common in both list1 and list2.

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4]

l3 = []
duplicates = []

for x in list1:
    if x not in list2:
        l3.append(x)
    else:
        duplicates.append(x)

print(l3)
print(duplicates)

# s1 = set(list1)
# s2 = set(list2)

# c = s1 & s2

# print(c)