#Extract words that start with a vowel
#Given a list of words words = ["apple", "banana", "orange", "grape", "kiwi"], create a list comprehension that includes only the words starting with a vowel (a, e, i, o, u).

words = ["apple", "banana", "orange", "grape", "kiwi"]
vow  = ("a","e","i","o","u")
for x in words:
    if x[0] in vow:                        #miostake : in keyword use 
        print("Vowels")
    else:
        print("Not Vowels")
print()
print("LIST COMPREHENSION :: ")
print()
new6 = [x for x in words if x[0] in vow]                 #if condition to use 
print(new6)