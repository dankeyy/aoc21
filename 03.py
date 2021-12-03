
from collections import Counter, defaultdict
from pprint import pprint
from operator import itemgetter

gamma = ''
epsilon = ''
c = defaultdict(Counter)
decimal_coversion = lambda x: int(x, 2)

with open('03.txt') as lines:
    for line in map(str.rstrip, lines):
        for i, bit in enumerate(line):
            c[i][bit] += 1

for v in c.values():
    most, least = map(itemgetter(0), v.most_common())
    gamma += most
    epsilon += least
gamma, epsilon = map(decimal_coversion, (gamma, epsilon))


print(gamma * epsilon)
