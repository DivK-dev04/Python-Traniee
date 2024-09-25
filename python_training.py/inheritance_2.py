class base:                                                 #parent class
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def display(self):                                      #method
        print(f"My name is {self.fname} {self.lname}")

class sub(base):
    pass                                                    #pass keyword to not give error 

class subs(base):                                           #another child class to inherit the properties of parent class
    def __init__(self,fname, lname):
        super().__init__(fname, lname)                      #super keyword use to represent the parent class

x = subs("NHZ", "INDIA")
x.display()