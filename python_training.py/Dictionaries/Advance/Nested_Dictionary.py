# Nested Dictionary
# Create a dictionary called company with the following structure:
# Task: Access and print the age of employee2.

company = {
    'name': 'TechCorp',
    'employees': {
        'employee1': {'name': 'Alice', 'age': 30, 'position': 'Developer'},
        'employee2': {'name': 'Bob', 'age': 25, 'position': 'Designer'}
    },
    'location': 'San Francisco'
}

# print(company)
print(company['employees']['employee2']['age'])