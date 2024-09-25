#Generate squares of numbers divisible by 4
#Write a list comprehension that generates the squares of numbers between 1 and 30, but only for numbers divisible by 4.

new7 = [x ** 2 for x in range(30) if x % 4 == 0]
print(new7)