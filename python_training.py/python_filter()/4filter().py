def a(x):
    return x.lower().startswith('a')                                #startswith() is a method, it will check the letter starting with 'a' or not

words = ['Apple', 'Banana', 'Avocado', 'Mango', 'Apricot', 'Grapes']
# Expected Output: ['Apple', 'Avocado', 'Apricot']

b = list(filter(a,words))

print(b)