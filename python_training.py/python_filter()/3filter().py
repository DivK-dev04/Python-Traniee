def odd(num):
    return num % 2 != 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [1, 3, 5, 7, 9]
oddy = list(filter(odd, numbers))

print(oddy)