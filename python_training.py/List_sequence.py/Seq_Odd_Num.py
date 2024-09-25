# # Sequence of Odd Numbers:
# # Create a list that starts with the number 1. Add the next odd number to the list until you have 25 odd numbers in total. Print the list.

# a = [1]
# while len(a) < 25:
#     odd = a[-1] + 2
#     a.append(odd)
# print(a)

def user():
    try:
        num = int(input("Enter the number : "))
        if num == 0:
            print("Enter value more than 0.")
            return
        
        a = [num]
        while len(a) < 25:
            if a[-1] % 2 == 0:
                odd = a[-1] + 1
                a.append(odd)
            else:
                odd = a[-1] + 2
                a.append(odd)
        print(a)
    except ValueError:
        print("Give Valid Input.")
user()