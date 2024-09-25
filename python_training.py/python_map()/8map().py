words = ['apple', 'banana', 'cherry', 'date']
# Expected Output: ['a', 'b', 'c', 'd']

def a(word):                                                 
    return word[0]
    
#f = list(map(lambda word: word[0], words)) 

f = list(map(a, words))
print(f)