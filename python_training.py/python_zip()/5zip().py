prices = [10, 20, 15]
quantities = [2, 3, 5]

t = sum(price * quantity for price, quantity in zip(prices, quantities))    #generators expression
print(t)
