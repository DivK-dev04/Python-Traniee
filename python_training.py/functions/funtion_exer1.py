#Write a program to print twin primes less than 1000. If two consecutive odd numbers are both prime then they are known as twin primes

def check_prime(num):                                    #check prime number

    num = int(num)

    if num <=1:                                           #check num is less than or equal to 1 
        print("less than 1 or eqaul to 1")
        return False
    elif num == 2:                                        # check num is eqaul to 2 
        print("it is 2 it is prime")
        return True
    elif num % 2 == 0:                                    # check num is divisible by 2 that measn it is even number
        print("it is even number")
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):            # main functionality to check prime number or not after 3 
        if num % i == 0:
            print(f"{num} is not prime")
            return False
    print(f"{num} is prime")
    return True

num = input("Enter the any number to check it is prime or not : ")   
check_prime(num)