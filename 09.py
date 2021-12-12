from pprint import pprint
from math import prod
from pathlib import Path

m = [[int(x) for x in list(line)] for line in Path('09.txt').read_text().splitlines()]
relative_neighbors = ((0,1), (0, -1), (1, 0), (-1, 0))
bounded = lambda x, rc: 0 <= x < rc
point = lambda p, m: m[p[0]][p[1]]


def adjacents(m, r, c):
    return ((r+i, c+j) for i, j in relative_neighbors
            if bounded((r+i), len(m)) and bounded(c+j, len(m[0])))


def low_points(m):
    return ((r,c) for r in range(len(m)) for c in range(len(m[0]))
            if all(m[r][c] < m[i][j] for i, j in adjacents(m, r, c)))


def p1(m):
    return sum(1 + m[r][c] for r, c in low_points(m))


def basins(m, p, seen=set()):
    seen.add(p)
    return sum(1 + basins(m, p, seen) for p in adjacents(m, *p)
               if p not in seen and point(p, m) != 9)


def p2(m):
    return prod(sorted((1+basins(m, p) for p in low_points(m)), reverse=True)[:3])


print(p1(m), p2(m))
