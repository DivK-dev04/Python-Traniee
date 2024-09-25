def g(a,b):                                             #position arguments
    print(f"Value of a : {a} , Value of b : {b}")
    return a+b
result = g(4,5)
print(result)

def greet(movie , character):                           #Keyword arguments
    print(f"{movie} : {character}")

greet(movie= "Jurassic Park", character= "T-Rex")