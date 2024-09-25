thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

tuple1 = ("Apple","banana","guava","grapes")
tuple2 = (11,22,33,44,55,66)
tuple3 = (111,"okay",123,2.55,"ok")
print(tuple1)
print(tuple2)
print(tuple3)

print(tuple1[1])
print(tuple2[2:4])

tuple1 = ("Apple","banana","guava","grapes")
y = list(tuple1)
y[1]="kiwi"
x = tuple(y)

print (x)

#join tuple

t = tuple1 + tuple2
print(t)
