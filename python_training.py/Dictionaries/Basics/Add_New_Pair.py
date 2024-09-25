# Add a New Key-Value Pair
# Add a new key-value pair to the student dictionary: 'graduation_year': 2025.
# Task: Print the updated dictionary.

student = { 'name': 'John' , 'age': 20 , 'major': 'Computer Science'}

print("Before : ",student)

# student.update({"graduation_year" : "2025"})
# print("After : ", student)
                                                                        #both the ways to do 
student ['graduation_year'] = ('2025')
print("After : ",student)