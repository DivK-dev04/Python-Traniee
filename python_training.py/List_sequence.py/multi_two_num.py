# a= [2,3]
# while len(a) < 5:
#         add = a[-1] * a[-2]
#         a.append(add)
# print(a)

def user_input():
        first = int(input("Enter the First Number : "))
        second = int(input("Enter the Second Number : "))

        while True:
                length = int(input("Enter the Length (MIN : 2), (MAX : 15) : "))
                if length > 2 and length <= 15:
                    break
                else:
                    print("ERROR :: Enter the Length between 2 and 15.")
        return first, second, length


def calc(first, second, length):
    a= [first, second]
    while len(a) < length:
            add = a[-1] * a[-2]
            a.append(add)
    print(f"THE FINAL OUTPUT : {a}")

first, second, length = user_input()

calc(first, second, length)