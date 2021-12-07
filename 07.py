def sigma(n):
    return int(n * (n + 1) / 2)


def avg(xs):
    return round(sum(xs) / len(xs))


def p1(xs):
    xs.sort()
    median = xs[len(xs) // 2]
    return sum(abs(x-median) for x in xs)


def p2(xs):
    return sum(sigma(abs(x-avg(xs))) for x in xs)


xs = [16,1,2,0,4,2,7,1,2,14]
print(p1(xs), p2(xs))
