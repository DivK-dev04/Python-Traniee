#1
all_names = ["SCOOBY","DOOBY","DOOBY","DO","DOOOOOOOO"]

new = list(map(str.lower, all_names))
print(new)


#2
deci = [3.1454654, 27.4565656, 0.06363017, 108.9435435, 56.164352345]

result = list(map(round, deci , range(1,7)))

print(result)


#3
def sq(num):
    return num ** 2

numbers = [1,2,3,4,5]

r = list(map(sq, numbers))
print(r)


#4  use a lambda function instead of defining a function separately.
numbers = [1, 2, 3, 4, 5]
re = map(lambda x: x ** 2, numbers)
print()
print("lambda function instead of defining a function separately")
print(list(re))

