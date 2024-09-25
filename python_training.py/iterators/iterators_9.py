#Using itertools.cycle() to Create a Repeating Iterator
import itertools

colors = ['red', 'green', 'blue']

cycle = itertools.cycle(colors)

for _ in range(5):
    print(next(cycle))