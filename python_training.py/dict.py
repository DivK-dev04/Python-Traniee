a = {"Company":"NineHertz","Position":"Trainee","Job":"Python Developer"}
print (a)
print(a["Company"])
print(a["Position"])
print(a["Job"])

thisdict = {                              #duplicates not allowed
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(a))                             #length of dictionaries
print(len(thisdict))

ax = {                                    
    "Company":"NineHertz",
    "Position":"Trainee",
    "Job":"Python Developer",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
    }

print(ax["Job"])
print(ax["year"])                         #access the items by keyname the square brackets

print(ax.get("brand"))                    #access the items by get() method also


print(ax.keys())
ax["Color"]=("Yellow")                    #add new key to the dictionaries
print(ax)


print(ax.values())
ax["Color"]=("Golden")                    #update values to the dictionaries as well as
ax["City"]=("Jaipur")                     #add new values to the dictionaries
print(ax)

print(ax.items())                         #print each items of dict 

if "car" in ax:                           #check if items is there or not
    print("yes it is there")
else:
    print("no insert it")


ax.update({"brand":"Mahindra"})           #update method for existing item in dict
print(ax)

ax.pop("year")                            #remove key:value pair both via pop() method
print(ax)

ax.popitem()                              #remove last inserted key:value pair in dict
print(ax)

del ax["brand"]                           #del remove specific name 
print(ax)


for x in ax:                               #only key names 
    print(x)

for x in ax:
    print("Only values =" ,ax[x])

xa = ax.copy()
print(xa)
print(ax)


############################################################################################

#Nested Dictionaries

nest = {
    "qw" : {"Language":"Python" , "Car":"Audi"},
    "er" : {"Language":"NodeJS" , "Car":"Mercedes"},
    "ty" : {"Lnaguage":"React" , "Car":"BMW"} 
}

print(nest["qw"]["Car"])