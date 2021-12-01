
# depths = [199 ,200 ,208 ,210 ,200 ,207 ,240 ,269 ,260 ,263]

with open('01.txt') as lines:
    depths = [int(l) for l in lines]


def solve(p1):
    w = 1 if p1 else 3 # if p2

    return sum(depths[i] < depths[i + w] for i in range(len(depths) - w))


print(solve(p1=True), solve(p1=False))
