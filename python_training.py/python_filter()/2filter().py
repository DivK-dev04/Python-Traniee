def three_words(word):
    return len(word)>3

words = ['cat', 'dog', 'elephant', 'rat', 'bat', 'hippo']

a = list(filter(three_words, words))

print(a)