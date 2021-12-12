import re
from pathlib import Path
from functools import reduce

lines = [line.strip() for line in Path("10.txt").read_text().splitlines()]
opening = "({[<"
pairs = ['()', '{}', '[]', '<>']

incomplete = lambda line: all(x in opening for x in line)
corrupt = lambda line: not incomplete(line)

def cleaned(line):
    return (line if all(p not in line for p in pairs)
        else cleaned(re.sub(r"(\(\))|(\{\})|(\[\])|(\<\>)", "", line)))


##################################################################################

scoresA = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def corrupt_score(line):
    line = cleaned(line)
    return 0 if incomplete(line) else next(scoresA[x] for x in line if x not in opening)


def p1(lines):
    return sum(map(corrupt_score, lines))

##################################################################################

scoresB = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,

}

def incomplete_score(line):
    line = cleaned(line)[::-1]
    return 0 if corrupt(line) else reduce(lambda acc, b: acc * 5 + scoresB[b], line, 0)


def p2(lines):
    scores = sorted(score for line in lines if (score := incomplete_score(line)) != 0)
    return scores[len(scores) // 2]

##################################################################################

print(p1(lines), p2(lines))
