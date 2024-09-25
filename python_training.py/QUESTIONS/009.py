#Extract even numbers and double them
#Given a list of numbers numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], write a list comprehension that extracts only the even numbers and doubles them.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new9 = [x + x for x in numbers if x % 2 == 0]
print(new9)