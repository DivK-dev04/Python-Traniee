class person:                                                                           #parent class / base class 
    def __init__(self, fname ,lname):
        self.first = fname
        self.second = lname 
    def printname(self):                                                                #printname method
        print(self.first , self.second)

class Student(person):                                                                  #inheritance - child class of person(parent class)
    def __init__(self,fname, lname, year):                                              #if have nothing in child class, use pass keyword to avoid error
        super().__init__(fname, lname)                                                  #super keyword for inherits the charctertics of parent class
        self.grad = year

    def welcome(self):                                                                  #method inside child class of parent class 
        print(f"Welcome {self.first} {self.second} of the graduation year {self.grad}")

fname = input("Enter the first name : ")                                                #taking input from user
lname = input("Enter the last name : ")                                                 #taking input from user
year = input("Graduation year : ")                                                      #taking input from user

x = Student(fname, lname, year)                                                         #x is object of person class

x.printname()
print(f"{x.grad}")
x.welcome()