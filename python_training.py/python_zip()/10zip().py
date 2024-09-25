a = ['A','B','C','D']
b = [1,2,3,4]
c = ['A',1,2,'B']
d = (11,22,33,44,55)

z = list(zip(a,b,c,d))
print(z)

from itertools import zip_longest

zipp = list(zip_longest(a,b,c,d, fillvalue="N/A"))
print()
print(zipp)