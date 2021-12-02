# moves = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

def operations(path='02.txt'):
    with open(path) as lines:
        for op, x in map(str.split, lines):
            yield op, int(x)


def solve():
    real_depth = aim_depth = pos = 0
    valid_ops = {'forward'} | (direction := {'up': -1, 'down': 1}).keys()

    for op, x in operations():
        assert op in valid_ops

        if op == 'forward':
            pos += x
            real_depth += aim_depth * x

        else: aim_depth += x * direction[op]

    return aim_depth * pos, real_depth * pos


print(*solve())
