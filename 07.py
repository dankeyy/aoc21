from math import ceil, floor
from statistics import mean, median

def sigma(n):
    return n * (n + 1) // 2


def p1(xs):
    m = median(xs)
    return sum(abs(x - m) for x in xs)


def p2(xs):
    def total_by(f):
        m = mean(xs)
        return sum(sigma(abs(f(x - m))) for x in xs)

    return min(total_by(ceil), total_by(floor))


xs = [16,1,2,0,4,2,7,1,2,14]
print(p1(xs))
print(p2(xs))
