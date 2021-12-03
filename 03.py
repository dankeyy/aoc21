from operator import mul
from pathlib import Path
from collections import Counter

decimal = lambda x: int(x, 2)
TABLE = Path('03.txt').read_text().splitlines()
LEN_ROW = len(TABLE[0])

def in_column(col: int, table: list[str]) -> Counter:
    """p1 & p2 helper, counts bits per column in table"""
    c = Counter()
    for line in table:
        c[line[col]] += 1
    return c

#################################################################################

def p1(table: list[str]=TABLE) -> int:
    counters: list[Counter] = [in_column(col, table) for col in range(LEN_ROW)]
    gamma = epsilon = ''

    for c in counters:
        (most, _), (least, _) = c.most_common()
        gamma += most
        epsilon += least

    return mul(*map(decimal, (gamma, epsilon)))

#################################################################################

def rating(bit_criteria: int, table: list[str]=TABLE) -> int:
    """Get rating value corresponding to given bit criteria (0: co2, 1: oxygen)"""
    buff = ''

    for i in range(1, LEN_ROW):
        if len(table) == 1: break

        (most, cmost), (least, cleast) = in_column(i - 1, table).most_common()
        if cmost == cleast: buff += str(bit_criteria)
        else: buff += most if bit_criteria else least

        table = [row for row in table if row.startswith(buff)]

    return decimal(table.pop())

def p2() -> int:
    return rating(1) * rating(0)

#################################################################################
print(p1(), p2())
