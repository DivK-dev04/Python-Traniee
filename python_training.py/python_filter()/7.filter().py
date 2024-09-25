def num(a):
    return a % 3 == 0 and a % 5 == 0                                             #use 'and' if want both condition to be true 

numbers = [15, 30, 45, 10, 22, 33, 60, 75, 21]
# Expected Output: [15, 30, 45, 60, 75]

x = list(filter(num, numbers))

print(x)