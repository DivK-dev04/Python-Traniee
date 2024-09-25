class parent:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calc(self):
        num3 = self.num1 + self.num2
        print(f"addition of two numbers : {num3}")

class student(parent):
    def __init__(self,num1, num2, grad_year):
        super().__init__(num1, num2)
        self.year = 1900
        self.grad_year = grad_year
        
x = student(2,5,2022)                                      #print(x.year) was not working bcoz x was of parent and year was declare din student class 
x.calc()
print(x.year)
print(x.grad_year)