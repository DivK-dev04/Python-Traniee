def st(a):
    return a != ''                                                  #not equal to to check which is not a space

strings = ['apple', '', 'banana', '', 'cherry', '', 'date']
# Expected Output: ['apple', 'banana', 'cherry', 'date']

x = list(filter(st, strings))

print(x)