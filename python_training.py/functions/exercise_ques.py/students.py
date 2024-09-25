class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, grades):
        self.grades.append(grades)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
    def display(self):
        print(f"Student : {self.name} , Average Grades : {self.average()}")

stud = Student("NHZ")
stud.add_grades(85)
stud.add_grades(90)
stud.display()