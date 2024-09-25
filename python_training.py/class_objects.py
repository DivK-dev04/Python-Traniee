#FIRST TRY
class car:                                             #making of class
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display(self):
        print(f"{self.brand} , {self.model} , {self.year}")

mycar = car("BMW","X-series","3012")                   #making of  object

mycar.display()


#SECOND TRY
class dog:                                             #making of class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"My dog {self.name} is {self.age} years old.")

doggy = dog("Buddy","6")                                 #making of class

doggy.bark()


#THIRD TRY
class cars:                                               #making of  object
    def __init__(self, model, year, brand, km):
        self.model = model
        self.year = year
        self.brand = brand
        self.km = km

    def vehicle(self):
        print(f"{self.model}, {self.year}, {self.brand}, {self.km}")

q = cars("BMW","2230","x","6783")                          #making of class

q.vehicle()


#FOURTH TRY
class student:                                             #making of  object
    def __init__(self, name, sem, score, course):
        self.name = name
        self.sem = sem
        self.score = score
        self.course = course

    def stud(self):
        print(f"{self.name}, {self.sem}, {self.score}, {self.course}")

school = student(f"Ris","8","90","MCA")                     #making of object

school.stud()