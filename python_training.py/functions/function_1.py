#greatest among 3 number


def func(x,y,z):
    x = int(x)
    y = int(y)
    z = int(z)

x = input("Enter the first number as x : ")
y = input("Enter the second number as y: ")
z = input("Enter the second number as z: ")

if x > y and x > z:
    print("X is great")
elif y > x and y > z:
    print("y is great")
else:
    print("greatest is z")

func(x,y,z)