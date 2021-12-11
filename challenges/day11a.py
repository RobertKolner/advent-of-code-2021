import sys

import numpy as np


def run(values_str: str):
    board = np.array([[int(v) for v in line] for line in values_str.split("\n") if line])

    flashes = 0
    for _ in range(100):
        board += 1

        while any(board.flat > 9):
            for y in range(board.shape[0]):
                for x in range(board.shape[1]):
                    if board[y, x] > 9:
                        board[y, x] = np.iinfo(board.dtype).min
                        board[max(0, y - 1) : y + 1 + 1, max(0, x - 1) : x + 1 + 1] += 1

        flashes += sum(board.flat < 0)
        board[board < 0] = 0

    return flashes


if __name__ == "__main__":
    print(run(sys.stdin.read()))
