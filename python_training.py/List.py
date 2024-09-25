a = ["Car","Bike","Buses","Airplane","Train"]
list1 = ["abc", 34, True, 40, "male"]

print(a)
print(len(a))
print(len(list1))
print(type(a))
print(a[2])

# print(a)
# a[4]="Bullet Trains"
# print(a)

ax = a.copy()            #use copy() method    #problem solve
ax[4]="Bullet Trains"
print(a)
print(ax)

ax.append("Ships")       #append()
print(ax)

a.append("Ships")
print(a)

a.insert(1,"Tractor")      #insert()
print(a)

a.extend(list1)           #extend()
print(a)

list1.remove(34)         #remove()
print(list1)

list1.pop(1)             #pop()
print(list1)

list1.clear()                #clear()
print(list1)

a = ["Car","Bike","Buses","Airplane","Train"]
for x in a:
    print(x)



m = ["HTML","CSS","JS","Python","Django"]           #sort()
n = [120,990,908,9.7,96]

m.sort()
n.sort()
print(m + n)

m.sort(reverse=True)
n.sort(reverse=True)
print(m + n)


q = ["Apple","guava","Orange","banana","grapes"]          #problem
print(q)
# q.sort()
# print(q)
q.sort(key = str.lower)
print(q)

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)



o = [1,2,3,4,5]
p = [11,22,33,44,55]

add_list = o + p
print(add_list)

#List comprehension

fruits = ["apple","orange","kiwi","mango","avacado","grapes"]
newfruits = []
for x in fruits:
    if "e" in x:
        newfruits.append(x)

print(newfruits)