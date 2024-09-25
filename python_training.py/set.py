a = {"11","22","33","44","11",11,11,23,23,45}
print(a)
print(len(a))

for x in a:           #for keyword indexing a sdirect index is not available in set
    print(x)

print("44" in a)       #using in keyword


a.add("100")
print(a)

b = {"pineapple", "mango", "papaya"}

a.update(b)
print(a)


set1 = {11,22,33,44,55,6677}
set2 = {22,77,88,9990,00}
set3 = {"Q","W","E","R","T","Y"}
#a = set1.union(set2)                                #can be done in both ways either this
a = set1 | set2                                      #or this by using -> ' | '
g = set1 | set2 | set3
print(a)
print(g)

e = set1.intersection(set2)                           #intresection method  either this 
r = set1 & set2                                       #or this
print(r)
print(e)