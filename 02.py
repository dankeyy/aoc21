
# moves = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']


def operations(path='02.txt'):
    with open(path) as lines:
        for op, x in map(str.split, lines):
            yield op, int(x)


def solve():
    real_depth = aim_depth = pos = 0
    bsignum = lambda cond: int(cond) or -1 # helper to determine direction

    for op, x in operations():
        assert op in {'forward', 'up', 'down'}

        if op == 'forward':
            pos += x
            real_depth += aim_depth * x

        else: aim_depth += x * bsignum(op == 'down')

    return real_depth * pos, aim_depth * pos


print(solve())
