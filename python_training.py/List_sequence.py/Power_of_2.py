# Sequence of Powers of 2:
# Create a list where the first number is 1, and each subsequent number is the double of the previous one. Continue this pattern until the list has 25 elements.
# Print the list.

# a = [1]
# while len(a) < 25:
#     mul = a[-1] * 2
#     a.append(mul)
# print(a)

def user_input():
    try:
        num = int(input("Enter first number of the list to start : "))
        return num
    except ValueError:
        return

def calc(num):
    try:
        a = [num]
        while len(a) < 25:
            mul = a[-1] * 2
            a.append(mul)

        print(a)
    except:
        print("ENTER VALID INPUT")
num = user_input()
calc(num)    