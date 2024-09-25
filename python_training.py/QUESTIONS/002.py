#take a list, find out duplicate value and how many of them, print new list without duplicates  

# a = [1,1,2,3,4,5,4,4,4,2,2,3,3]
# new_a = []
# for x in set(a):                                        #by using set()....(don't use set)
#     print(f"{x} , {a.count(x)}")
#     new_a.append(x)

# print(new_a)

a = [1,1,2,3,5,4,4,4,2,2,3,3]
new = []
# duplicates = []

for x in a:
    # print(x)
    if x not in new:
        new.append(x)
    # elif x not in duplicates:                              #for creating a list to store duplicates also
    #     duplicates.append(x)
        
print(f"{new}")
# print(f"Duplicate values: {duplicates}")