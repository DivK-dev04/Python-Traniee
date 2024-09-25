#Flatten a list of lists
#Given a list of lists list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8]], write a list comprehension to flatten this list into a single list containing all the elements.

lists = [[1, 2, 3], [4, 5], [6, 7, 8]]

new12 = [x for sublist in lists for x in sublist]
print(new12)