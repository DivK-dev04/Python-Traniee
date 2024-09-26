# Reverse a Dictionary
# Given the dictionary grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'A'}, reverse it so that the keys are the grades and the values are lists of names of students who received each grade.
# Task: Print the reversed dictionary.

grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'A'}

rev_grades = {}

for student, grades in grades.items():
    if grades in rev_grades:
        rev_grades[grades].append(student)
    else:
        rev_grades[grades] = [student]

print(rev_grades)