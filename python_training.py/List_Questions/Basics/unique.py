#Write code to get a list of unique elements from list1 and list2.

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

uni = []

l = list1 + list2
print(l)                                        #[3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99, 6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]    
for x in l:
    if x not in uni:
        uni.append(x)

print(uni)