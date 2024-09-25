def palindrome(word):
    return word == word[::-1]                                                          #Compare word with its reverse

words = ['racecar', 'hello', 'level', 'world', 'madam', 'python']

a = list(filter(palindrome, words))

print(a)