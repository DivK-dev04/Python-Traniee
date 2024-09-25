# 1. Sum of Previous Two Numbers (Fibonacci Variant):
# Create a list where the first two numbers are 1 and 4. Each subsequent number is the sum of the previous two numbers.
# Continue the sequence until the list has 25 elements. Print the list.


def user_input():
    try:
        first = int(input("Enter the First number : "))
        second = int(input("Enter the Second number : "))

        while True:
            length = int(input("Enter the Length (MIN : 2), (MAX : 25) : "))
            if length > 2:
                break
            else:
                print("Valid Length.")
        return first, second, length
    except:
        print("ENTER THE VALID INPUT.")

def calc(first,second, length):
    a = [first,second]
    while len(a) < length:
        add = a[-1] + a[-2]
        a.append(add)
    print(a)

first , second , length = user_input()
calc(first , second , length)