#List Comprehension
#1.
fruits = ["aaa","bbb","ccc","ddd","eee"]

new1 = [x.upper() for x in fruits]

print(new1)

#2.
#new_list = [expression for x in some_iterable if condition]                     #syntax
new2 = [x for x in range(10) if x > 2 and x < 8]

print(new2)

#3.
#[expression_if_true1 if condition1 else (expression_if_true2 if condition2 else expression_if_false) for item in iterable]                #syntax
new3 = [x * 2 if x < 5 else (x * 3 if x > 8 else x) for x in range(10)]
print(new3)