# Check for a Key and Add if Not Present
# Given the dictionary car = {'make': 'Toyota', 'model': 'Corolla', 'year': 2010}, check if the key 'mileage' exists. If not, add it with a value of 120000.
# Task: Print the final dictionary.

car = {'make': 'Toyota', 'model': 'Corolla', 'year': 2010}

if 'mileage' in car:
    print("It exists.")
    print(car)
else:
    print("No, its not there")
    car['milage'] = 12000
    print(f"Updated with 'mileage' key : car = {car}")