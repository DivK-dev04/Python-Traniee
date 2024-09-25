def mul(a , b):
    a = int(a)
    b = int(b)

    product = a*b
    return product

def table(number):
    print(f"Multiplication Table of the number : {number}")

    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")

product = mul(2,3)
table(product)
