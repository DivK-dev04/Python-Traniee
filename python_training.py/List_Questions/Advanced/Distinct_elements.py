#Write code to count how many distinct elements are common in both list1 and list2.

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

common_elements = []

for x in list1:                             #"Distinct elements" means each element should only be counted once, regardless of how many times it appears.
    if x in list2 and x not in common_elements:
        common_elements.append(x)

count_common_elements = len(common_elements)
print(common_elements)
print(f"Number of distinct common elements: {count_common_elements}")
