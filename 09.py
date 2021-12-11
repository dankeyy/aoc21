from pprint import pprint
from pathlib import Path

m = [[int(x) for x in list(line)] for line in Path('09test.txt').read_text().splitlines()]
rows, cols = len(m), len(m[0])

relative_neighbors = ((0,1), (0, -1), (1, 0), (-1, 0))
bounded = lambda x, rc: 0 <= x < rc


def adjacents(m, r, c):
    return (m[r+i][c+j] for i, j in relative_neighbors
            if bounded((r+i), rows) and bounded(c+j, cols))

def p1(m):
    return sum(1 + m[r][c] for r in range(rows) for c in range(cols)
               if all(m[r][c] < adj for adj in adjacents(m, r, c)))




print(p1(m))
