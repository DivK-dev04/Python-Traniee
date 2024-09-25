import array

x = dir(array)                                                                #Using dir()
print("Using dir() : ")
for item in x:
    print(item)                                                               #to print content of array module


print("Using __dict__ : ")
for name in array.__dict__:                                                   #Using __dict__
    print(name)