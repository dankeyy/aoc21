from heapq import heappop, heappush


GRID = [[*map(int, line.rstrip())] for line in open('15.txt')]


def solve(ratio):
    w, h = len(GRID[0]), len(GRID)
    end = (w * ratio -1, h * ratio -1)

    bounded   = lambda x, y: 0 <= x < h*ratio and 0 <= y < w*ratio
    neighbors = lambda x, y: ((x+1, y), (x, y+1), (x-1, y), (x, y-1))

    graph = {(x, y) : GRID[x][y] for x in range(h) for y in range(w)}
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


print(solve(ratio=1)) # part 1
print(solve(ratio=5)) # part 2
