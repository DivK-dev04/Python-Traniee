#Replace vowels in a string with '*'
#Given a string text = "replace vowels", write a list comprehension to create a new string where all vowels are replaced with '*'.

text = "replace vowels"

vow  = ("a","e","i","o","u")
# new13 = [x.replace() for x in text if x == vow]
new13 = [x if x not in vow else '*' for x in text]
new133 = ''.join(new13)
print(new133)