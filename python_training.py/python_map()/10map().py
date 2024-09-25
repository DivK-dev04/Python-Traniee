pairs = [(1, 2), (3, 4), (5, 6)]

def sum_pair(pair):
    return pair[0] + pair[1]

sums = list(map(sum_pair, pairs))

print(sums)