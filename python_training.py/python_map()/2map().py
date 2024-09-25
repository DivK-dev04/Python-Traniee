#Double the elements in a list

numbers = [1, 3, 5, 7, 9]                 #list

def double(num):                          #function to double the number
    return num * 2 

new = list(map(double, numbers))          #map() function used
print(new)