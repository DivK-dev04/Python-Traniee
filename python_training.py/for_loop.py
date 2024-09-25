fruits = ["A","B","C","D","E"]
for x in fruits:
    print(x)

print(type(fruits))

a = "bannanana"
for x in a:
    print(x)

fruits = ["A","B","C","D","E"]           #break after print
for x in fruits:
    print(x)
    if x == "D":
        break


fruits = ["A","B","C","D","E"]            #break before print
for x in fruits:
    if x == "D":
        break
    print(x)


fruits = ["A","B","C","D","E"]            #continue in for loop
for x in fruits:
    if x == "D":
        continue
    print(x)


for x in range(11):                        #range()
   print(x)


#NESTED LOOP

ab = ["abc","def","ghi","jkl","mno"]
dc = ["pqr","stu","vwx","yza","abb"]

for x in ab:
    for y in dc:
        print(x,y)