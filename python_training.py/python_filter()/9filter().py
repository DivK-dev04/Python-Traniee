def st(a):
    return a.isalpha()

strings = ['apple', 'banana123', 'grape', 'ch3rry!', 'mango']
# Expected Output: ['apple', 'grape', 'mango']

x = list(filter(st, strings))

print(x)