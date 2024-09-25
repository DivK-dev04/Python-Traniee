def mul():
    a = [1,2,3,4,5]

    total = 1
    for x in a:
        total *= x

    print("product of the list : " , total)
mul()


def multi(num1 , num2):
    num1 = int(num1)
    num2 = int(num2)

    num3 = num1 * num2 
    print("Multiplication of two number is : ",num3)

multi(5,6)
