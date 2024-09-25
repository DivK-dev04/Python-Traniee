# Loop Through a Dictionary
# Given the dictionary book = {'title': '1984', 'author': 'George Orwell', 'pages': 328, 'year': 1949}, write a loop that prints each key-value pair in the format:
# key: value.

book = {'title': '1984', 'author': 'George Orwell', 'pages': 328, 'year': 1949}

for k,v in book.items():
    print(f"{k} : {v}")