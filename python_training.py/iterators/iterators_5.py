#Infinite Iterator with itertools.count()
#Python’s itertools library provides several useful iterators. One example is count(), which generates an infinite sequence of numbers.

import itertools                                            #import library

counter = itertools.count(start=1, step=2)                  #count iterators in itertools
for _ in range(5):                                          #for loop till range 5
    print(next(counter))