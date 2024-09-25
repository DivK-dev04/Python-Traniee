#Filter even numbers and multiply them by 3
#Write a list comprehension that takes a range of numbers from 1 to 20 and includes only even numbers, but multiplies them by 3 before adding them to the list.

new4 = [x * 3 for x in range(20) if x % 2 == 0]
print(f" #4 : {new4}")