import sys


def run(values_str: str):
    lines = [line.strip() for line in values_str.split("\n")]
    numbers = [int(n) for n in lines[0].split(',') if n]
    boards = [[int(value) for line in lines[6 * n + 2:6 * n + 8] if line for value in line.split() if value] for n in
              range((len(lines[2:]) + 1) // 6)]

    for number in numbers:
        for board in boards:
            for i, value in enumerate(board):
                if value != number:
                    continue

                board[i] = None
                if any([
                    any(all(board[row * 5 + col] is None for row in range(5)) for col in range(5)),
                    any(all(board[row * 5 + col] is None for col in range(5)) for row in range(5)),
                ]):
                    return sum(value for value in board if value is not None) * number


if __name__ == "__main__":
    print(run(sys.stdin.read()))
