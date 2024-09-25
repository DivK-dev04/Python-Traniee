def odd(num):
    return num > 10

numbers = [4, 11, 18, 3, 9, 15, 7, 21]
# Expected Output: [11, 18, 15, 21]

x = list(filter(odd, numbers))

print(x)