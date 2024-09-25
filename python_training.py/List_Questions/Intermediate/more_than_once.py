def find_duplicates_in_both(list1, list2):
    # Create dictionaries to count occurrences in both lists
    l1 = {}
    l2 = {}

    # Count occurrences in list1
    for x in list1:
        if x in l1:
            l1[x] += 1
        else:
            l1[x] = 1

    # Count occurrences in list2
    for x in list2:
        if x in l2:
            l2[x] += 1
        else:
            l2[x] = 1

    # Find elements that appear more than once in both lists
    duplicates_in_both = []
    for x in l1:
        if x in l2 and l1[x] > 1 and l2[x] > 1:
            duplicates_in_both.append(x)

    return duplicates_in_both

# Test the function
list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11, 7]

duplicates = find_duplicates_in_both(list1, list2)
print(duplicates)

