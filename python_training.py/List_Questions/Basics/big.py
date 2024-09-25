list_name = input("Enter the name of the list you want : ")

a = []

def input_values():
    global a
    print("Enter integer value between 10 to 15 : ")

    while True:
        try:
            a = list(map(int, input(f"Enter values for {list_name}").split()))

            if len(a) < 10 or len(a) > 15:
                print("Error : enter 10 to 15 values")
                a = []
            elif any(x<0 for x in a):
                print("Error : negative numbers are not allowed")
                a = []
            else:
                break
        except ValueError:
            print("Error : Enter valid integer value")
            a = []

try:
    input_values()

    rep = []

    [rep.append(x) for x in a if x not in rep]

    print(f"Original List : {a}")
    print(f"Without duplicates : {rep}")
    print(len(rep))
except Exception as e:
    print(f"Uexpected error : {e}")