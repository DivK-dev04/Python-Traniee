#Write code to find all unique elements that are common in both list1 and list2.

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

l1 = {}
l2 = {}

for x in list1:
    if x in l1:
        l1[x] += 1
    else:
        l1[x] = 1

for x in list2:
    if x in l2:
        l2[x] += 1
    else:
        l2[x] = 1

uni_com = []
for x in l1:
    if x in l2 and l1[x] == 1 and l2[x] == 1:
        uni_com.append(x)

print(uni_com)