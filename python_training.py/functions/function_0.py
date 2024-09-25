def myfunc():
    print("FIRST")

myfunc()

def func(fname):                  #arguments
    print(fname + " Arguments")

func("hello")
func("NHZ")

def ok(name, age):                #parameters and arguments
    print(name, age, "ok")

ok("div", 26)

def ad(num1, num2):                #function practice

    num1 = int(num1)
    num2 = int(num2)
    
    operation = input("Enter 'add' for addition or 'subtract' for subtraction: ")
    
    if operation == 'add':
        print("Addition = ", num1 + num2)
    elif operation == 'subtract':
        print("Subtraction = ", num1 - num2)
    else:
        print("Invalid operation. Please choose 'add' or 'subtract'.")

num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

ad(num1, num2)






