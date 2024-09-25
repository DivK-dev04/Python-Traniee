#Write functions to find both the intersection (common elements) and the union (all unique elements) of list1 and list2.

def intersectionnn(list1, list2):      #The intersection() method will return a new set, that only contains the items that are present in both sets.

    set1 = set(list1)                                   # Create sets from the lists to find common elements
    set2 = set(list2)

    i = set1 & set2                                         # Intersection: common elements
    return list(i)

def unionnn(list1, list2):    #The union() method returns a new set with all items from both sets.

    set1 = set(list1)                                        # Create sets from the lists to find all unique elements
    set2 = set(list2)

    u = set1 | set2                                          # Union: all unique elements
    return list(u)

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

intersection = intersectionnn(list1, list2)
union = unionnn(list1, list2)

print(intersection)
print(union)