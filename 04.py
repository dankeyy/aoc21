from itertools import islice

def game_input(path='04test.txt'):
    boards = []

    with open(path) as f:
        numbers_drawn = next(f).rstrip().split(',')
        next(f)

        while board := ''.join(islice(f, 5)).split():
            next(f, None)
            boards.append(board)

    return numbers_drawn, boards


_marked    = lambda seq: set(seq) == {'x'}
_row_bingo = lambda n, board: _marked(board[n*5: (n+1)*5])
_col_bingo = lambda n, board: _marked(board[n::5])

def bingo(board):
    return any(_col_bingo(n, board) or _row_bingo(n, board) for n in range(5))

def sum_unmarked(board) -> int:
    return sum(int(cell) for cell in board if cell != 'x')

def try_mark(b, n):
    try:
        hit = b.index(n)
        b[hit] = 'x'
    except ValueError: pass


def iterate_until_bingo(numbers, boards):
    for n in numbers:
        for b in boards:
            try_mark(b, n)

            if bingo(b):
                return int(n) * sum_unmarked(b)


def solve1():
    return iterate_until_bingo(*game_input())


def solve2():
    numbers, boards = game_input()
    didnt_win = {*range(len(boards))}

    for nid, n in enumerate(numbers):
        for bid, b in enumerate(boards):

            if bid in didnt_win:
                try_mark(b, n)

                if bingo(b):
                    if len(didnt_win) == 1:
                        loser = boards[ didnt_win.pop() ]
                        return iterate_until_bingo(numbers[nid:], [loser])

                    didnt_win -= {bid}


print(solve1(), solve2())
