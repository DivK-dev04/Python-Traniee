def mul(x,y):
    return x*y

list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Expected Output: [4, 10, 18]

a = list(map(mul, list1, list2))
print(a)