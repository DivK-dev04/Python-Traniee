#Create a list of tuples with index and value
#Given a list nums = [10, 20, 30, 40, 50], use list comprehension to create a list of tuples where each tuple contains the index and the value from the list.

nums = [10, 20, 30, 40, 50]

new8 = [(index, value) for index, value in enumerate(nums)]
print(new8)