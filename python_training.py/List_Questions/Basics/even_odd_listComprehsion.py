#even numbers with List Comprehension 
a = [11,22,3,4,5,66,7,8,90,24,12,13,14,15,1515,2424,2409]
even = []

for x in a:                                         #traditional way to do
    if x % 2 == 0:
        even.append(x)
even.sort()
print("Using for loop :",even)

evens = [x for x in a if x % 2 == 0]                  #List Comprehension way to do it
evens.sort()
print("List Comprehension of even in list: ",evens)
s = sum(evens)
print("Sum of sorted evens : ",s)

odds = [x for x in a if x % 2 != 0]                   # Odds using List comprehension
odds.sort()
print("Odds in a[] : ", odds)

sq = [x**2 for x in a]                                    #square of original list
sq.sort()
print("Square of original list : ",sq)

sqr_even = [x**2 for x in a if x % 2 == 0]             #Square even numbers
sqr_even.sort()
print("Square even numbers : ",sqr_even)

sqr_odd = [x**2 for x in a if x%2 != 0]
sqr_odd.sort()
print("Square odd numbers : ", sqr_odd)