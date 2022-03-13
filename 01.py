with open("01.txt") as lines:
    depths = [*map(int, lines)]


def solve(w):
    return sum(depths[i] < depths[i + w] for i in range(len(depths) - w))


print(solve(1)) # p1
print(solve(3)) # p2
