#alrready inputted list

def sums():
    a = [1,2,3,4,5,6,7,8,9,10]
    for x in a:
        print(x)
    total = sum(a)
    print("Total of list is = ",total)
sums()


#input from user
def calc():
    numbers =[]

    print("User needs to input five numbers")
    for i in range(6):                    
        num = int(input(f"Enter the number {i + 1}: "))
        numbers.append(num)

    total = sum(numbers)                               #due to in the for loop just writing mistake  the error was coming 

    print("Numbers Enter by User : ", numbers)
    print("Total of that number : ",total)


calc()

