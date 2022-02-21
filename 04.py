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
    won = set()

    for n in numbers:
        for i, board in enumerate(boards):
            if i not in won:

                try: board[board.index(n)] = 'x'
                except ValueError: pass

                if score := bingo(board):
                    score *= int(n)
                    won.add(i)
                    yield score


def solve():
    first = last = next(play(*game_input()))
    for last in play(*game_input()):
        pass

    return first, last

print(solve())
