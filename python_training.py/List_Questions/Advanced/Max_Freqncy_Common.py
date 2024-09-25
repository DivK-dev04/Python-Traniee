#Write a function to find the element that appears most frequently among the common elements of list1 and list2.

# list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
# list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

# l3 = list1 + list2
# print(l3)
# common = []

# for x in l3:
#     if x in list2:
#         common.append(x)

# print(common)

# list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
# list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

# common_elements = []


# # Iterate through list1 and check how many times each element appears in both lists
# for x in list1:
#     if x in list2:
#         common_elements.append(x)
#         # list2.remove(x)  # Remove element from list2 to handle duplicates

# print(common_elements)

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

# Combine both lists
combined = list1 + list2

common_elements = []

# Iterate over the combined list and check for duplicates
for x in combined:
    if combined.count(x) > 1:  # If an element appears more than once, add it to the common_elements
        common_elements.append(x)

print(common_elements)


