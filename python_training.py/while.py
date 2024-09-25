i = 1                 #while loop
while i < 10:
    print(i)
    i = i+1


print("Break Statement")
i = 1                 #Break (( after 7 ))
while i < 10:
    print(i)
    if i == 7:
        break
    i = i+1


print("Continue Statement")
i = 0
while i < 10:
    i = i+1
    if i == 3:
        continue
    print(i)