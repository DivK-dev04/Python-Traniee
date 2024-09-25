#Python program to interchange first and last elements in a list
a = [1,2,3,4,5]
z = []
c = a.copy()                              # use copy() method to create copy of list
c[0],c[-1]=c[-1],c[0]   # python support simultaneous assignment
print(c)

print("Original List : ", a)
c.reverse()                                      #reverse
print("Reverse List: ",c)

b = [1,2,3,4,5]

temp = b[0]
b[0] = b[-1]
b[-1] = temp

print("The other method")
print(b)


a = [1,2,3,4,5]                         #double list number
for x in a:
    x = x * 2
    z.append(x)

print(a)
print(z)

q = [1,3,5,7,9,11,11]
u = []
r = sum(q)                      #sum of all list
s = max(q)                       # max among the list
t = list(set(q))                #duplicate remove using set
print(r , s ,t)

#same remove the duplicate without using set

for x in q:
    if x not in u:
        u.append(x)

print("without set : ",u)