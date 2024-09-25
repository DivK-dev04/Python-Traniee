class python:
    year = 1976
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def calc(self):
        num3 = self.num1 + self.num2
        print(num3)

x = python(2,5)
x.calc()

for name in python.__dict__:
    print(name)

y = dir(python)
print("dir()###################################################### : ")
for items in y:
    print(items)