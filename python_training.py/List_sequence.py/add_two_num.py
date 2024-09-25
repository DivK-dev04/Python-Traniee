# a= [2,3]
# while len(a) < 25:
#         add = a[-1] + a[-2]
#         a.append(add)
# print(a)


def user_input():
    try:
        first = int(input("Enter the first number : "))
        second = int(input("Enter the secomd number : "))

        while True:
            length = int(input("Enter the length of the List : "))
            if length > 2:
                break
            else:
                print("Give minimun 2 length")
                 # break

        a = [first, second]
        while len(a) < length:
            add = a[-1] + a[-2]
            a.append(add)

        print(a)
    except ValueError:
        print("Enter the valid Integer")

user_input()