from math import ceil, floor

def sigma(n):
    return n * (n + 1) // 2


def avg(xs):
    return sum(xs) / len(xs)


def p1(xs):
    xs.sort()
    median = xs[len(xs) // 2]
    return sum(abs(x-median) for x in xs)


def p2(xs):
    total_by = lambda f: sum(sigma(abs(f(x-avg(xs)))) for x in xs)
    return min(total_by(ceil), total_by(floor))

xs = [16,1,2,0,4,2,7,1,2,14]
print(p1(xs), p2(xs))
