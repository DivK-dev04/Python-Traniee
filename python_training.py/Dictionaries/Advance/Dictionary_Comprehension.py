# Dictionary Comprehension
# Given a list of numbers numbers = [1, 2, 3, 4, 5], create a dictionary where each number is a key and its square is the value.
# Task: Print the resulting dictionary.

numbers = [1, 2, 3, 4, 5]
num_sq = {}

for x in numbers:
    # if x in num_sq:
        z = x ** 2
        # print(z)
        # num_sq.append(z)
        num_sq[x] = (z)

print(num_sq)