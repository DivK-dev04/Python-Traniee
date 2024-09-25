a = "Ninehertz"
b = "The Ninehertz India  "
c = "is Best in India."
print(a)
print("The Best company in Jaipur is ",a)
print(len(a))
print(a.upper())
print(a.lower())
print(b.replace("N","Z"))
print(a[1])

# Using for loop
for x in "Ninehertz":
    print(x)


# Modify
print("Best" in b)
print("The" in b)

print(a[2:5])
print(a[2:])

print(b.strip())

# Concatenate
print(b + c)

# F-Strings
age = 26
txt = f"Common age in the Company is {age}"
print(txt)

# Using function
age = 26

def myfunc():
    age = 27
    print("Correction in the age :", age)

myfunc()
print("Previous age:",age)

ax = "Python Developer"

def secfunc():
    global ax
    a = "Developer"
    print(ax)

secfunc()

z = 26
x = 24

if z > x:
    print("It is the greatest =",z)
else:
    print("Other is gretest")