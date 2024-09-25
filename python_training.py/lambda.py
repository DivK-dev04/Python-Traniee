x = lambda a , b : a + b
print(x(4,5))

x = lambda a , b ,c : a*b*c
print(x(4,5,6))

def lam(n):
    return lambda a : a * n
double = lam(2)

print(double(10))