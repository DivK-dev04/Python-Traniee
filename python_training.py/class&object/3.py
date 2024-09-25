class students:
    def __init__(self,stud_id,stud_name,class_name):
        self.stud_id = stud_id
        self.stud_name = stud_name
        self.class_name = class_name

stud = students("12345678889999990","NHZ","Development")

print(stud.stud_id)
print(stud.stud_name)
print(stud.class_name)

print(stud.__dict__)
print(students.__dict__)