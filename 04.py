from pathlib import Path

def game_input(path='04.txt'):
    numbers, *boards = Path(path).read_text().split('\n\n')

    numbers = numbers.strip().split(',')
    boards = [*map(str.split, boards)]
    return numbers, boards


def bingo(board):
    for n in range(5):
        all_marked_row = all(square == 'x' for square in board[n * 5: (n+1) * 5])
        all_marked_col = all(square == 'x' for square in board[n::5])

        if all_marked_row or all_marked_col:
            unmarked_board_count = sum(int(cell) for cell in board if cell != 'x')

            return unmarked_board_count


def play(numbers, boards):
    for n in numbers:
        for i, board in enumerate(boards):

            try: board[board.index(n)] = 'x'
            except ValueError: pass

            if score := bingo(board):
                score *= int(n)
                yield i, score


def p1():
    _, score = next(play(*game_input()))
    return score


def p2():
    numbers, boards = game_input()
    game = play(numbers, boards)
    losers = {*range(len(boards))}

    while len(losers) != 1:
        i, _ = next(game)
        losers -= {i}

    _, score = next(play(numbers, [boards[losers.pop()]]))
    return score

    
print(p1(), p2())
