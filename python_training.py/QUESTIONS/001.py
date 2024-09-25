#a is list, when user press enter then the value to be print ,on each press one element of list should be print

a = [1,1,2,3,4,5,4,4,4,2,2,3,3]

iterator = iter(a)

while True:
    input("Press Enter")

    try:
        print(next(iterator))
    except StopIteration:
        print("list ends")
        break
