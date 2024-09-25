#Write functions to find both the intersection (common elements) and the union (all unique elements) of list1 and list2.
def intersectionnn(list1, list2):
    inter = []
    for x in list1:
        if x in list2 and x not in inter:
            inter.append(x)
    return inter
    
def unionnn(list1, list2):
    union = list1.copy()
    for x in list2:                 #checking with list2 first, union means combination of both set but no duplicates value will be there
        if x not in union:
            union.append(x)
    return union

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

intersection = intersectionnn(list1, list2)
unions = unionnn(list1, list2)

print(intersection)
print(unions)