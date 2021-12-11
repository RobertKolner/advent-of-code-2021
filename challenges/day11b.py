import sys

import numpy as np


def run(values_str: str):
    board = np.array([[int(v) for v in line] for line in values_str.split("\n") if line])

    step = 0
    while True:
        step += 1
        board += 1

        while any(board.flat > 9):
            for y in range(board.shape[0]):
                for x in range(board.shape[1]):
                    if board[y, x] > 9:
                        board[y, x] = np.iinfo(board.dtype).min
                        board[max(0, y - 1) : y + 1 + 1, max(0, x - 1) : x + 1 + 1] += 1

        board[board < 0] = 0
        if all(board.flat == 0):
            return step


if __name__ == "__main__":
    print(run(sys.stdin.read()))
