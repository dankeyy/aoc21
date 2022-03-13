import re
from pathlib import Path
from functools import reduce
from statistics import median


LINES = [line for line in Path("10.txt").read_text().splitlines()]


def cleaned(line):
    return (line if all(p not in line for p in ('()', '{}', '[]', '<>'))
        else cleaned(re.sub(r"(\(\))|(\{\})|(\[\])|(\<\>)", "", line)))


def incomplete(line):
    return all(x in "({[<" for x in line)


def corrupt(line):
    return not incomplete(line)


def corrupt_score(line):
    line = cleaned(line)
    scoresA = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    return (0 if incomplete(line)
        else next(scoresA[x] for x in line if x not in "({[<"))


def incomplete_score(line):
    line = cleaned(line)[::-1]
    scoresB = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    return (0 if corrupt(line)
        else reduce(lambda acc, b: acc * 5 + scoresB[b], line, 0))


p1 = sum(map(corrupt_score, LINES))
print(p1)

p2 = median(score for line in LINES if (score := incomplete_score(line)) != 0)
print(p2)
