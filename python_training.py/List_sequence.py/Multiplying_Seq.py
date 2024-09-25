# 4. Multiplying Sequence:
# Start with a list [1]. For the next 24 elements, multiply the previous number by 3 to get the next number in the list. Print the list.

# a = [1]
# while len(a) < 25:
#     mul = a[-1] * 3
#     a.append(mul)
# print(a)

def user():
    try:
        num = int(input("Enter the Number to start the process : "))
        length = int(input("Enter the length : "))

        return num, length
    except:
        print("ENTER VALID INPUT")

def calc(num, length):
    a = [num]
    while len(a) < length:
        mul = a[-1] * 3
        a.append(mul)
    print(a)

num , length = user()
calc(num, length)