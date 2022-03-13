def operations(path="02.txt"):
    with open(path) as lines:
        for op, x in map(str.split, lines):
            yield op, int(x)


def solve():
    real_depth = aim_depth = pos = 0
    # forward is not aim/ depth related
    direction = {
        "up"  : -1,
        "down":  1,
    }

    for op, x in operations():
        if op == "forward":
            pos += x
            real_depth += aim_depth * x
        else:
            aim_depth += x * direction[op]

    return aim_depth * pos, real_depth * pos


p1, p2 = solve()
print(p1)
print(p2)
