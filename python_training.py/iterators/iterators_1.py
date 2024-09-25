mytuple = ("a","b","c")
myitv = iter(mytuple)

print("This is iter() and next() : ")
print(next(myitv))                                 #this is with iter() and next()
print(next(myitv))
print(next(myitv))

print("This is for loop.")
for x in mytuple:                                  #this is with for loop
    print(x)