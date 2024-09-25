a = [11, 22, 3, 4, 5, 66, 7, 8, 90, 24, 12, 13, 14, 15, 66, 24, 2409, 38, 47, 66, 67, 89, 24, 1203, 24, 12, 12, 12, 22]
# o = 12
# oz = [x for x in a if x != o]
# print(oz)
# print(len(oz))

#take a list, find out duplicate value and how many of them, print new list without duplicates  

# for x in a:                                                  #for loop working
#     if x not in rep:
#         rep.append(x)
rep = []
[rep.append(x) for x in a if x not in rep]           

print(rep)
print(len(rep))