from pathlib import Path
from collections import defaultdict


def dfs(node, twice, graph, seen=frozenset()):
    if node == 'end': return 1

    if node in seen and node.islower() and twice and node != 'start':
        return sum(dfs(neighbor, False, graph, seen | {node}) for neighbor in graph[node])

    if node not in seen or node.isupper():
        return sum(dfs(neighbor, twice, graph, seen | {node}) for neighbor in graph[node])

    return 0


def main():
    m = [tuple(x.split('-')) for x in Path('12.txt').read_text().splitlines()]

    graph = defaultdict(set)
    for a, b in m:
        graph[a].add(b)
        graph[b].add(a)

    print(dfs(node='start', graph=graph, twice=False)) # p1
    print(dfs(node='start', graph=graph, twice=True)) # p2


main()

# 5178
# 130094
