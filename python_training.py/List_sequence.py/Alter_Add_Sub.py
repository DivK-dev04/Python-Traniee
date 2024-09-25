# Alternating Addition and Subtraction:
# Start with a list [10]. For the next 24 elements, alternate between adding 5 and subtracting 3 from the previous number.
# Print the final list of 25 elements.

# a = [10]
# while len(a) < 25:
#     alter_add = a[-1] + 5
#     a.append(alter_add)
#     alter_sub = a[-1] - 3
#     a.append(alter_sub)
    
# print(a)

def calc():
    try:
        num = int(input("Enter the one number to start the list : "))
        a = [num]
        while len(a) < 25:
            1/0
            alter_add = a[-1] + 5
            a.append(alter_add)
            alter_sub = a[-1] - 3
            a.append(alter_sub)
        print(a)
    except Exception as e:
        print("ENTER VALID INPUT FOR CALCULATION.",str(e))
calc()