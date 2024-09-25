#Generate the cubes of odd numbers
#Write a list comprehension to create a list of cubes of numbers from 1 to 15, but only for odd numbers.

new11 = [x ** 3 for x in range(1, 15) if x % 2 != 0]
print(new11)