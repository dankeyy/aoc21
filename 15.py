from heapq import heappop, heappush
from pathlib import Path

grid = [[*map(int, list(x))] for x in Path('15.txt').read_text().splitlines()]
neighbors = lambda x, y: ((x+1, y), (x, y+1), (x-1, y), (x, y-1))


def solve(grid, ratio=5):
    w, h = len(grid[0]), len(grid)
    end = (w * ratio -1, h * ratio -1)

    graph = {(x, y) : grid[x][y] for x in range(h) for y in range(w)}
    bounded = lambda x, y: 0 <= x < h*ratio and 0 <= y < w*ratio
    heap = [(0, (0,0))]
    visited = set()

    while heap:
        risk_so_far, cell = heappop(heap)
        for neighbor in neighbors(*cell):
            if bounded(*neighbor) and neighbor not in visited:

                x, y = neighbor
                risk = graph.get((x % h, y % w))
                risk = sum(divmod(x // h + y // w + risk, 10))

                if neighbor == end:
                    return risk + risk_so_far

                visited.add(neighbor)
                heappush(heap, (risk + risk_so_far, neighbor))


print(solve(grid, ratio=1)) # part 1
print(solve(grid, ratio=5)) # part 2
