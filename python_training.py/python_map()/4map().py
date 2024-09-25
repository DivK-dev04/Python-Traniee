#Add corresponding elements from two lists

def add(x,y):
    return x + y

list1 = [1, 2, 3]
list2 = [4, 5, 6]

new = list(map(add , list1 , list2))
print(new)
