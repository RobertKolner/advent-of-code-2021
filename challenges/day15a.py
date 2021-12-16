import heapq
import sys


def run(values_str: str):
    board = [[int(v) for v in line] for line in values_str.split("\n") if line]
    end = (len(board[-1]) - 1, len(board) - 1)
    queue = []
    heapq.heappush(queue, (0, (0, 0)))
    added_coords = set()

    while True:
        risk, coordinates = heapq.heappop(queue)

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = (coordinates[0] + dx, coordinates[1] + dy)
            if (x, y) == end:
                return risk + board[y][x]
            if (x, y) in added_coords:
                continue
            added_coords.add((x, y))
            if end[0] >= x >= 0 and end[1] >= y >= 0:
                heapq.heappush(queue, (risk + board[y][x], (x, y)))


if __name__ == "__main__":
    print(run(sys.stdin.read()))
