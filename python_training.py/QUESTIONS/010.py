#Convert strings to uppercase
#Given a list of strings strings = ["hello", "world", "python", "is", "fun"], write a list comprehension to convert all strings in the list to uppercase.

strings = ["hello", "world", "python", "is", "fun"] 

new10 = [x.upper() for x in strings]
print(new10)